
function build () {
  opts = {
    fontSize: 20,
    angle: 0.1, /// The span of the gauge arc
    lineWidth: 0.44, // The line thickness
    pointer: {
      length: 0.9, // Relative to gauge radius
      strokeWidth: 0.035 // The thickness
    },
    colorStart: '#6FADCF', // Colors
    colorStop: '#8FC0DA', // just experiment with them
    strokeColor: '#E0E0E0', // to see which ones work best for you
    staticLabels: {
      font: '20px sans-serif', // Specifies font
      labels: [0, 100], // Print labels at these values
      color: '#000000', // Optional: Label text color
      fractionDigits: 0 // Optional: Numerical precision. 0=round off.
    },
    radiusScale: 0.9
  }
  canvas = document.getElementById(
    document.currentScript.getAttribute('data-canvasid')
  )
  gauge = new Gauge(canvas).setOptions(opts) // create sexy gauge!
  document.getElementById(document.currentScript.getAttribute('data-canvasid')).removeAttribute('style')
  gauge.maxValue = 100 // set max gauge value
  gauge.setMinValue(0) // set min value
  gauge.animationSpeed = 1
  gauge.set(
    parseInt(document.currentScript.getAttribute('data-gauge'))
  ) // set actual value
}

build()
