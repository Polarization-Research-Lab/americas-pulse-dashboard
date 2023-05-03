const canvas = document.getElementById(
  document.currentScript.getAttribute('data-canvasid')
)

function build () {
  const canvasid = document.currentScript.getAttribute('data-canvasid')
  const datasource = '/americas-pulse-dashboard/assets/data/violence-sankey.json'

  fetch(datasource)
    .then((request) => request.json())
    .then((data) => {
      const chart = new Chart(
        canvas,
        {
          type: 'sankey',
          data: {
            datasets: [{
              label: 'My sankey',
              data: data.data,
              colorFrom: (c) => data.colors[c.dataset.data[c.dataIndex].from],
              colorTo: (c) => data.colors[c.dataset.data[c.dataIndex].to],
              labels: data.labels,
              priority: {
              },
              /* optional column overrides */
              column: {
              },
              size: 'max' // or 'min' if flow overlap is preferred
            }]
          },
          options: {
            maintainAspectRatio: false,
            scales: {
              x: { min: -0.4, max: 5.5 },
              y: { min: -data.max * 0.3, max: data.max + data.max * 0.3 }
            },
            plugins: {
              annotation: {
                annotations: [
                  { content: ['Protesting', 'w/o Permit'], xValue: 0, yValue: data.max + (data.max * 0.13), type: 'label', font: { size: 18 } },
                  { content: ['Vandalism'], xValue: 1, yValue: data.max + (data.max * 0.13), type: 'label', font: { size: 18 } },
                  { content: ['Assault'], xValue: 2, yValue: data.max + (data.max * 0.13), type: 'label', font: { size: 18 } },
                  { content: ['Arson'], xValue: 3, yValue: data.max + (data.max * 0.13), type: 'label', font: { size: 18 } },
                  { content: ['Assault w/', 'Deadly Weapon'], xValue: 4, yValue: data.max + (data.max * 0.13), type: 'label', font: { size: 18 } },
                  { content: ['Murder'], xValue: 5, yValue: data.max + (data.max * 0.13), type: 'label', font: { size: 18 } }
                ].concat(data.annotations)
              },
              datalabels: {
                color: 'blue',
                labels: {
                  title: {
                    font: {
                      weight: 'bold'
                    }
                  },
                  value: {
                    color: 'green'
                  }
                }
              }
            }
          }
        }
      )
    })
}
build()
