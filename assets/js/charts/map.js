
function build () {
  const canvasid = document.currentScript.getAttribute('data-canvasid')
  const datasource = document.currentScript.getAttribute('data-source')

  const scaleminlabel = document.currentScript.getAttribute('data-scaleminlabel')
  const scalemaxlabel = document.currentScript.getAttribute('data-scalemaxlabel')

  function rankTextFormat (val) {
    if (parseInt(val) == 1) {
      return val + 'st'
    } else if (parseInt(val) == 2) {
      return val + 'nd'
    } else if (parseInt(val) == 3) {
      return val + 'rd'
    // } else if (parseInt(val) > 3) {
    } else {
      return val + 'th'
    }
  }

  fetch(datasource)
    .then((r) => r.json())
    .then((data) => {
      fetch('/americas-pulse-dashboard/assets/data/states-10m.json')
        .then((r) => r.json())
        .then((us) => {
          const canvas = document.getElementById(canvasid)
          const nation = ChartGeo.topojson.feature(us, us.objects.nation).features[0]
          const states = ChartGeo.topojson.feature(us, us.objects.states).features
          const chart = new Chart(canvas.getContext('2d'), {
            type: 'choropleth',
            data: {
              labels: states.map((d) => d.properties.name),
              datasets: [
                {
                  label: 'Counties',
                  outline: nation,
                  data: states.map((d) => ({
                    feature: d,
                    value: data.vals[d.properties.name.toLowerCase()],
                    rank: data.ranks[d.properties.name.toLowerCase()]
                  }))
                }
              ]
            },
            options: {
              // responsive: true,
              maintainAspectRatio: false,
              plugins: {
                tooltip: {
                  callbacks: {
                    label: function (context) {
                      val = ['Score: ' + context.element.$context.raw.value, 'Rank: ' + rankTextFormat(context.element.$context.raw.rank)]
                      return val
                    }
                  }
                },
                legend: {
                  display: false
                }
              },
              layout: {
            	padding: {
                  right: 50
                }
              },
              scales: {
                projection: {
                  axis: 'x',
                  projection: 'albersUsa'
                },
                color: {
                // min: 0,
                // max: 100,
                  axis: 'x',
                  quantize: 100,
                  interpolate: function (val) {
                    s = evaluate_cmap(val, 'viridis', true)
                    return 'rgb(' + s[0] + ',' + s[1] + ',' + s[2] + ',1)'
                  // return evaluate_cmap(val, 'viridis', true)
                  },
                  // interpolate: function (val) {
                  // console.log(evaluate_cmap(val, 'viridis', true))
                  // return evaluate_cmap(val, 'viridis', true)
                  // return Array([0,200,0])
                  // },
                  // interpolate: 'viridis',
                  // display: false,
                  legend: {
                    position: 'bottom-right',
                    align: 'right'
                  },
                  ticks: {
                    font: {
                      weight: 'bold',
                      size: 15,
                      color: 'rgba(0,0,0,1)'
                    },
                    count: 5,
                    // minRotation: 35,
                    callback: function (label, index, labels) {
                      if (index === 4) {
                        return scalemaxlabel
                      // return '😡'
                      }
                      if (index === 0) {
                        return scaleminlabel
                      // return '😇'
                      }
                    }
                  }
                }
              }
            }
          })

          canvas.addEventListener('click', function () {
        	console.log('clicked')
          })
        })
    })
}
build()
