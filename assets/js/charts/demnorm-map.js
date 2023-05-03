const canvasid_affpolmap = document.currentScript.getAttribute('data-canvasid')

fetch('/assets/data/states-10m.json')
  .then((r) => r.json())
  .then((us) => {
    canvas = document.getElementById(canvasid_affpolmap)

    const nation = ChartGeo.topojson.feature(us, us.objects.nation).features[0]
    const states = ChartGeo.topojson.feature(us, us.objects.states).features
    // const counties = ChartGeo.topojson.feature(us, us.objects.counties).features;

    // counties.map((d) => {console.log(d.properties.name)})

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
              value: Math.random() * 11
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
