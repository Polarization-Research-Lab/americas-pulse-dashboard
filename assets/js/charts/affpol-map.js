
function build () {
  const canvasid = document.currentScript.getAttribute('data-canvasid')
  const datasource = document.currentScript.getAttribute('data-source')

  fetch(datasource)
    .then((r) => r.json())
    .then((data) => {
      fetch('/assets/data/states-10m.json')
        .then((r) => r.json())
        .then((us) => {
          canvas = document.getElementById(canvasid)

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
                    value: data.all[d.properties.name]
                  }))
                }
              ]
            },
            options: {
              plugins: {
                color: false,
                legend: {
                  display: false
                }
              },
              layout: {
            	padding: 0
              },
              scales: {
                projection: {
                  axis: 'x',
                  projection: 'albersUsa'
                },
                color: {
                  axis: 'x',
                  quantize: 5,
                  legend: {
                    position: 'bottom-right',
                    align: 'right'
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
