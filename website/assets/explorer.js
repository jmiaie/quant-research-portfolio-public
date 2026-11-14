/* Interactive power explorers for the research site.
   No dependencies and no third-party requests: the data is assets/data/power.json,
   built from the project repositories' committed power-study results. Colours come
   from the CSS custom properties in site.css, so the charts follow the theme toggle. */
(function () {
  "use strict";

  var SVG_NS = "http://www.w3.org/2000/svg";
  var W = 560; // viewBox width; narrowed on small screens so labels stay legible

  function svgEl(name, attrs, parent) {
    var node = document.createElementNS(SVG_NS, name);
    for (var key in attrs) {
      if (Object.prototype.hasOwnProperty.call(attrs, key)) node.setAttribute(key, attrs[key]);
    }
    if (parent) parent.appendChild(node);
    return node;
  }

  function el(name, className, text, parent) {
    var node = document.createElement(name);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    if (parent) parent.appendChild(node);
    return node;
  }

  function pct(value) {
    if (value >= 0.995) return "100%";
    if (value < 0.01 && value > 0) return (value * 100).toFixed(1) + "%";
    return Math.round(value * 100) + "%";
  }

  function clear(node) {
    while (node.firstChild) node.removeChild(node.firstChild);
  }

  function linePath(points) {
    return points
      .map(function (p, i) {
        return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1);
      })
      .join(" ");
  }

  /* Shared frame: a percentage y-axis from 0 to 100% with the 80% target marked. */
  function frame(height, label) {
    var m = { top: 18, right: 78, bottom: 46, left: 44 };
    var svg = svgEl("svg", {
      class: "viz-svg",
      viewBox: "0 0 " + W + " " + height,
      role: "img",
      "aria-label": label
    });
    var plotH = height - m.top - m.bottom;
    var plotW = W - m.left - m.right;
    function y(value) {
      return m.top + plotH * (1 - value);
    }
    [0, 0.5, 1].forEach(function (tick) {
      svgEl(
        "line",
        { class: tick ? "viz-grid" : "viz-zero", x1: m.left, x2: W - m.right, y1: y(tick), y2: y(tick) },
        svg
      );
      svgEl("text", { class: "viz-tick", x: m.left - 8, y: y(tick) + 4, "text-anchor": "end" }, svg).textContent =
        Math.round(tick * 100) + "%";
    });
    svgEl("line", { class: "viz-target", x1: m.left, x2: W - m.right, y1: y(0.8), y2: y(0.8) }, svg);
    svgEl("text", { class: "viz-tick", x: W - m.right + 6, y: y(0.8) + 4 }, svg).textContent = "80% target";
    return { svg: svg, m: m, plotH: plotH, plotW: plotW, y: y };
  }

  function pointerX(svg, event) {
    var box = svg.getBoundingClientRect();
    return ((event.clientX - box.left) / box.width) * W;
  }

  /* ---------- Stat-arb: detection rate by spread half-life ---------- */

  function settingLabel(s) {
    var pairs = s.k === 1 ? "1 true pair" : s.k + " true pairs";
    return pairs + ", hedge ratio " + s.beta + ", leg volatility " + s.sigma * 100 + "% a day";
  }

  function statarb(root, data) {
    var settings = data.settings;
    var start = 0;
    settings.forEach(function (s, i) {
      if (s.k === 1 && s.beta === 1 && s.sigma === 0.01) start = i;
    });

    var controls = el("div", "explorer-controls", null, root);
    var label = el("label", "explorer-label", "Simulation setting", controls);
    var select = el("select", "explorer-select", null, label);
    settings.forEach(function (s, i) {
      var option = el("option", null, settingLabel(s), select);
      option.value = String(i);
    });
    select.value = String(start);

    var readout = el("p", "explorer-readout", null, root);
    readout.setAttribute("aria-live", "polite");
    var holder = el("div", "explorer-chart", null, root);
    var details = el("details", "explorer-table", null, root);
    el("summary", null, "Show the numbers", details);
    var table = el("table", null, null, details);

    var state = null;
    holder.addEventListener("pointermove", function (event) {
      if (!state) return;
      var i = Math.floor((pointerX(state.svg, event) - state.left) / state.band);
      if (i < 0 || i >= state.count) i = null;
      if (i !== state.active) draw(state.index, i);
    });
    holder.addEventListener("pointerleave", function () {
      if (state && state.active !== null) draw(state.index, null);
    });

    function draw(index, active) {
      var s = settings[index];
      var points = s.points;
      clear(holder);
      var f = frame(250, "Detection rate by spread half-life for " + settingLabel(s));
      var svg = f.svg;
      var band = f.plotW / points.length;
      function x(i) {
        return f.m.left + band * (i + 0.5);
      }
      var upper = points.map(function (p, i) {
        return [x(i), f.y(p.hi)];
      });
      var lower = points
        .map(function (p, i) {
          return [x(i), f.y(p.lo)];
        })
        .reverse();
      svgEl("path", { class: "viz-s1-band", d: linePath(upper.concat(lower)) + " Z" }, svg);
      svgEl(
        "path",
        {
          class: "viz-s1-line viz-nofill",
          d: linePath(
            points.map(function (p, i) {
              return [x(i), f.y(p.power)];
            })
          )
        },
        svg
      );
      points.forEach(function (p, i) {
        svgEl("text", { class: "viz-label", x: x(i), y: f.y(0) + 17, "text-anchor": "middle" }, svg).textContent =
          String(p.half_life);
        var dot = svgEl(
          "circle",
          { class: "viz-s1-dot" + (i === active ? " is-active" : ""), cx: x(i), cy: f.y(p.power), r: i === active ? 7 : 5 },
          svg
        );
        svgEl("title", {}, dot).textContent = p.half_life + " days: " + pct(p.power);
        if (i === active || (active === null && (i === 0 || i === 1))) {
          svgEl(
            "text",
            { class: "viz-value viz-strong", x: x(i) + 9, y: f.y(p.power) - 9, "text-anchor": "start" },
            svg
          ).textContent = pct(p.power);
        }
      });
      if (active !== null) {
        svgEl(
          "line",
          { class: "viz-cross", x1: x(active), x2: x(active), y1: f.m.top, y2: f.y(0) },
          svg
        );
      }
      svgEl(
        "text",
        { class: "viz-tick", x: f.m.left + f.plotW / 2, y: f.y(0) + 38, "text-anchor": "middle" },
        svg
      ).textContent = "Spread half-life, trading days";

      holder.appendChild(svg);
      state = { index: index, active: active, svg: svg, left: f.m.left, band: band, count: points.length };

      var shown = active === null ? 0 : active;
      var p = points[shown];
      readout.textContent =
        "At a " +
        p.half_life +
        "-day half-life the screen admits a truly cointegrated pair " +
        pct(p.power) +
        " of the time (95% interval " +
        pct(p.lo) +
        " to " +
        pct(p.hi) +
        ").";

      clear(table);
      var head = el("tr", null, null, el("thead", null, null, table));
      ["Half-life (days)", "Detection rate", "95% interval"].forEach(function (h) {
        el("th", null, h, head);
      });
      var body = el("tbody", null, null, table);
      points.forEach(function (q) {
        var row = el("tr", null, null, body);
        el("td", null, String(q.half_life), row);
        el("td", null, pct(q.power), row);
        el("td", null, pct(q.lo) + " to " + pct(q.hi), row);
      });
    }

    select.addEventListener("change", function () {
      draw(Number(select.value), null);
    });
    draw(start, null);
  }

  /* ---------- Options: coverage-test power by number of forecasts ---------- */

  function options(root, data) {
    var ns = data.n;
    var series = [
      { key: "1.5", name: "1.5× the target", css: "s1" },
      { key: "2", name: "2× the target", css: "s2" },
      { key: "3", name: "3× the target", css: "s3" }
    ];
    var maxN = ns[ns.length - 1];
    var lo = Math.log10(5);
    var hi = Math.log10(maxN);
    var current = 12;

    var controls = el("div", "explorer-controls", null, root);
    var label = el("label", "explorer-label", "Number of forecasts in the backtest", controls);
    var slider = el("input", "explorer-range", null, label);
    slider.type = "range";
    slider.min = "0";
    slider.max = "1000";
    slider.step = "1";
    var presets = el("div", "explorer-presets", null, controls);
    [
      [12, "12 (2024, 2025)"],
      [95, "95 (development)"],
      [250, "250 (one year, daily)"],
      [2500, "2,500 (2015–2025, daily)"]
    ].forEach(function (preset) {
      var button = el("button", "explorer-chip", preset[1], presets);
      button.type = "button";
      button.addEventListener("click", function () {
        set(preset[0]);
      });
    });

    var legend = el("div", "explorer-legend", null, root);
    series.forEach(function (s) {
      var item = el("span", "explorer-key", null, legend);
      el("span", "explorer-swatch explorer-swatch--" + s.css, null, item);
      el("span", null, "True breach rate " + s.name, item);
    });

    var holder = el("div", "explorer-chart", null, root);
    var readout = el("div", "stat-row explorer-stats", null, root);
    readout.setAttribute("aria-live", "polite");

    function toSlider(n) {
      return Math.round(((Math.log10(n) - lo) / (hi - lo)) * 1000);
    }
    function fromSlider(value) {
      var n = Math.round(Math.pow(10, lo + (value / 1000) * (hi - lo)));
      return Math.max(5, Math.min(maxN, n));
    }

    var geo = null;
    function fromPointer(event) {
      var px = Math.max(geo.left, Math.min(geo.left + geo.width, pointerX(geo.svg, event)));
      var n = Math.round(Math.pow(10, lo + ((px - geo.left) / geo.width) * (hi - lo)));
      return Math.max(5, Math.min(maxN, n));
    }
    function onPointer(event) {
      if (!geo) return;
      if (event.type === "pointerdown" || event.pointerType === "mouse" || event.buttons) {
        var n = fromPointer(event);
        if (n !== current) set(n);
      }
    }
    holder.addEventListener("pointermove", onPointer);
    holder.addEventListener("pointerdown", onPointer);

    function draw() {
      clear(holder);
      var f = frame(270, "Chance the coverage test flags a mis-calibrated VaR, by number of forecasts");
      var svg = f.svg;
      function x(n) {
        return f.m.left + ((Math.log10(n) - lo) / (hi - lo)) * f.plotW;
      }
      [10, 30, 100, 300, 1000].forEach(function (tick) {
        svgEl("line", { class: "viz-grid", x1: x(tick), x2: x(tick), y1: f.m.top, y2: f.y(0) }, svg);
        svgEl("text", { class: "viz-tick", x: x(tick), y: f.y(0) + 16, "text-anchor": "middle" }, svg).textContent =
          tick.toLocaleString("en-US");
      });
      series.forEach(function (s) {
        var values = data.power[s.key];
        var points = [];
        for (var i = 0; i < ns.length; i++) {
          if (ns[i] >= 5) points.push([x(ns[i]), f.y(values[i])]);
        }
        svgEl("path", { class: "viz-" + s.css + "-line viz-nofill", d: linePath(points) }, svg);
      });
      svgEl("line", { class: "viz-cross", x1: x(current), x2: x(current), y1: f.m.top, y2: f.y(0) }, svg);
      series.forEach(function (s) {
        var value = data.power[s.key][current - 1];
        svgEl("circle", { class: "viz-" + s.css + "-dot", cx: x(current), cy: f.y(value), r: 5.5 }, svg);
      });
      svgEl(
        "text",
        { class: "viz-tick", x: f.m.left + f.plotW / 2, y: f.y(0) + 38, "text-anchor": "middle" },
        svg
      ).textContent = "Number of forecasts (log scale)";
      holder.appendChild(svg);
      geo = { svg: svg, left: f.m.left, width: f.plotW };

      clear(readout);
      series.forEach(function (s) {
        var tile = el("div", "stat", null, readout);
        el("span", "stat-value", pct(data.power[s.key][current - 1]), tile);
        el(
          "span",
          "stat-label",
          "chance of catching a breach rate " + s.name + ", with " + current.toLocaleString("en-US") + " forecasts",
          tile
        );
      });
    }

    function set(n) {
      current = n;
      slider.value = String(toSlider(n));
      slider.setAttribute("aria-valuetext", n.toLocaleString("en-US") + " forecasts");
      draw();
    }
    slider.addEventListener("input", function () {
      current = fromSlider(Number(slider.value));
      slider.setAttribute("aria-valuetext", current.toLocaleString("en-US") + " forecasts");
      draw();
    });
    set(current);
  }

  /* ---------- Sentiment: smallest detectable gain by number of events ---------- */

  function sentiment(root, data) {
    var lo = Math.log10(100);
    var hi = Math.log10(100000);
    var current = data.n_published;

    function mde(n) {
      return data.mde_multiplier * data.se_hat * Math.sqrt(data.n_published / n);
    }
    function share(n) {
      return mde(n) / data.baseline_log_loss;
    }

    var controls = el("div", "explorer-controls", null, root);
    var label = el("label", "explorer-label", "Number of filing events in the test", controls);
    var slider = el("input", "explorer-range", null, label);
    slider.type = "range";
    slider.min = "0";
    slider.max = "1000";
    slider.step = "1";
    var presets = el("div", "explorer-presets", null, controls);
    [
      [197, "197 (published)"],
      [515, "515"],
      [2060, "2,060"],
      [100000, "100,000"]
    ].forEach(function (preset) {
      var button = el("button", "explorer-chip", preset[1], presets);
      button.type = "button";
      button.addEventListener("click", function () {
        set(preset[0]);
      });
    });
    var holder = el("div", "explorer-chart", null, root);
    var readout = el("div", "stat-row explorer-stats", null, root);
    readout.setAttribute("aria-live", "polite");

    function toSlider(n) {
      return Math.round(((Math.log10(n) - lo) / (hi - lo)) * 1000);
    }
    function fromSlider(value) {
      return Math.round(Math.pow(10, lo + (value / 1000) * (hi - lo)));
    }

    var geo = null;
    function onPointer(event) {
      if (!geo) return;
      if (event.type === "pointerdown" || event.pointerType === "mouse" || event.buttons) {
        var px = Math.max(geo.left, Math.min(geo.left + geo.width, pointerX(geo.svg, event)));
        var n = Math.round(Math.pow(10, lo + ((px - geo.left) / geo.width) * (hi - lo)));
        if (n !== current) set(n);
      }
    }
    holder.addEventListener("pointermove", onPointer);
    holder.addEventListener("pointerdown", onPointer);

    function draw() {
      clear(holder);
      var height = 240;
      var m = { top: 18, right: 78, bottom: 46, left: 44 };
      var plotH = height - m.top - m.bottom;
      var plotW = W - m.left - m.right;
      var top = 0.025;
      var svg = svgEl("svg", {
        class: "viz-svg",
        viewBox: "0 0 " + W + " " + height,
        role: "img",
        "aria-label": "Smallest detectable log-loss gain by number of events"
      });
      function x(n) {
        return m.left + ((Math.log10(n) - lo) / (hi - lo)) * plotW;
      }
      function y(value) {
        return m.top + plotH * (1 - Math.min(value, top) / top);
      }
      [0, 0.01, 0.02].forEach(function (tick) {
        svgEl("line", { class: tick ? "viz-grid" : "viz-zero", x1: m.left, x2: W - m.right, y1: y(tick), y2: y(tick) }, svg);
        svgEl("text", { class: "viz-tick", x: m.left - 8, y: y(tick) + 4, "text-anchor": "end" }, svg).textContent =
          Math.round(tick * 100) + "%";
      });
      [100, 1000, 10000, 100000].forEach(function (tick) {
        svgEl("line", { class: "viz-grid", x1: x(tick), x2: x(tick), y1: m.top, y2: y(0) }, svg);
        svgEl("text", { class: "viz-tick", x: x(tick), y: y(0) + 16, "text-anchor": "middle" }, svg).textContent =
          tick.toLocaleString("en-US");
      });
      var points = [];
      for (var i = 0; i <= 200; i++) {
        var n = Math.pow(10, lo + (i / 200) * (hi - lo));
        points.push([x(n), y(share(n))]);
      }
      svgEl("path", { class: "viz-s1-line viz-nofill", d: linePath(points) }, svg);
      svgEl("line", { class: "viz-cross", x1: x(current), x2: x(current), y1: m.top, y2: y(0) }, svg);
      svgEl("circle", { class: "viz-s1-dot", cx: x(current), cy: y(share(current)), r: 5.5 }, svg);
      svgEl(
        "text",
        { class: "viz-tick", x: m.left + plotW / 2, y: y(0) + 38, "text-anchor": "middle" },
        svg
      ).textContent = "Number of events (log scale)";
      holder.appendChild(svg);
      geo = { svg: svg, left: m.left, width: plotW };

      clear(readout);
      var a = el("div", "stat", null, readout);
      el("span", "stat-value", (share(current) * 100).toFixed(share(current) < 0.001 ? 3 : 2) + "%", a);
      el("span", "stat-label", "smallest log-loss gain detectable, as a share of the baseline", a);
      var b = el("div", "stat", null, readout);
      el("span", "stat-value", mde(current).toFixed(4), b);
      el("span", "stat-label", "the same gain in nats per event", b);
      var c = el("div", "stat", null, readout);
      el("span", "stat-value", current.toLocaleString("en-US"), c);
      el("span", "stat-label", "events in the test" + (current === data.n_published ? " (as published)" : ""), c);
    }

    function set(n) {
      current = Math.max(100, Math.min(100000, n));
      slider.value = String(toSlider(current));
      slider.setAttribute("aria-valuetext", current.toLocaleString("en-US") + " events");
      draw();
    }
    slider.addEventListener("input", function () {
      current = fromSlider(Number(slider.value));
      slider.setAttribute("aria-valuetext", current.toLocaleString("en-US") + " events");
      draw();
    });
    set(current);
  }

  var builders = { statarb: statarb, options: options, sentiment: sentiment };

  function init() {
    var roots = document.querySelectorAll("[data-explorer]");
    if (!roots.length) return;
    var url = roots[0].getAttribute("data-src");
    if (roots[0].clientWidth && roots[0].clientWidth < 430) W = 380;
    fetch(url)
      .then(function (response) {
        if (!response.ok) throw new Error("HTTP " + response.status);
        return response.json();
      })
      .then(function (data) {
        Array.prototype.forEach.call(roots, function (root) {
          var kind = root.getAttribute("data-explorer");
          clear(root);
          builders[kind](root, data[kind]);
        });
      })
      .catch(function () {
        Array.prototype.forEach.call(roots, function (root) {
          clear(root);
          el("p", "explorer-fallback", "The interactive chart could not load. The figure above shows the headline numbers.", root);
        });
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
