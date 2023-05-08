function build () {
  var canvasid_affpolhist = document.currentScript.getAttribute('data-canvasid')
  var datasource = document.currentScript.getAttribute('data-source')

  fetch(datasource)
    .then((request) => request.json())
    .then((data) => {
      var canvas = document.getElementById(canvasid_affpolhist)
      var xticks = [0, 20, 40, 60, 80, 100]
      var chart = new Chart(
        canvas.getContext('2d'),
        {
          type: 'line',
          data: {
            labels: data.x,
            datasets: [
              {
                label: 'Feelings towards Democrats',
                data: data.demtherm,
                color: 'blue',
                borderColor: 'rgba(19, 105, 235,.95)',
                backgroundColor: 'rgba(19, 105, 235,.8)',
                tension: 0.2,
                borderWidth: 4,
                pointRadius: 0,
                fill: true
              },
              {
                label: 'Feelings towards Republicans',
                data: data.reptherm,
                color: 'red',
                borderColor: 'rgba(247, 5, 33,.95)',
                backgroundColor: 'rgba(247, 5, 33,.8)',
                tension: 0.2,
                borderWidth: 4,
                pointRadius: 0,
                fill: true
              }
            ]
          },
          // yMax: Math.max(Math.max(data['demtherm']), Math.max(data['reptherm'])),
          options: {
            responsive: true,
            maintainAspectRatio: false,
            // animation: false,
            plugins: {
              legend: {
                // display: false,
                position: 'bottom'
              },
              annotation: {
                annotations: [
                  {
                    type: 'line',
                    yMin: 0,
                    yMax: 15, // <-- arbitrary; just get it to cover the whole plot
                    xMin: data.demtherm_avg,
                    xMax: data.demtherm_avg,
                    borderColor: 'rgba(19, 105, 235,.95)',
                    borderWidth: 2,
                    borderDash: [6, 6]
                  },
                  {
                    type: 'line',
                    yMin: 0,
                    yMax: 15, // <-- arbitrary; just get it to cover the whole plot
                    xMin: data.reptherm_avg,
                    xMax: data.reptherm_avg,
                    borderColor: 'rgba(247, 5, 33,.95)',
                    borderWidth: 2,
                    borderDash: [6, 6]
                  }
                ]
              }
            },
            scales: {
              x: {
                grid: { display: false },
                min: 0,
                max: 100,
                ticks: {
                  callback: function (value, index, ticks) {
                    if (xticks.includes(Math.round(value))) {
                      if (value === 0) {
                        return [value]//, '😡']
                      } else if (value === 100) {
                        return [value]//, '😍']
                      } else {
                        return value
                      }
                    }
                  },
                  font: {
                    size: 20
                  }
                }
              },
              y: {
                min: 0,
                max: Math.max(Math.max.apply(Math, data.demtherm), Math.max.apply(Math, data.reptherm)) * 1.1,
                grid: { display: false },
                ticks: { display: false }
              }
            }
          }
        }
      )
    }
  )
}

build()
