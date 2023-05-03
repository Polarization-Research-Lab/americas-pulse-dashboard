function build () {
  const canvasid_affpolhist = document.currentScript.getAttribute('data-canvasid')
  const datasource = '/americas-pulse-dashboard/assets/data/demnorm-lines.json'

  fetch(datasource)
    .then((request) => request.json())
    .then((data) => {
      const canvas = document.getElementById(canvasid_affpolhist)
      const xticks = [0, 20, 40, 60, 80, 100]
      const chart = new Chart(
        canvas.getContext('2d'),
        {
          type: 'line',
          data: {
            labels: data.x,
            datasets: [
              { label: ['Ignoring', 'Court Judges'], data: data.norm_judges, tension: 0.2, borderWidth: 4, pointRadius: 0, hidden: false, borderColor: 'teal' },
              { label: ['Reducing the # of', 'Polling Stations'], data: data.norm_polling, tension: 0.2, borderWidth: 4, pointRadius: 0, hidden: true, borderColor: 'green' },
              { label: ['Using', 'Executive Orders'], data: data.norm_executive, tension: 0.2, borderWidth: 4, pointRadius: 0, hidden: true, borderColor: 'orange' },
              { label: ['Censorship'], data: data.norm_censorship, tension: 0.2, borderWidth: 4, pointRadius: 0, hidden: true, borderColor: 'purple' },
              { label: ['Party Loyalty in', 'the Face of', 'Election Denial'], data: data.norm_loyalty, tension: 0.2, borderWidth: 4, pointRadius: 0, hidden: true, borderColor: 'grey' }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: false,
            scales: {
              y: {
                min: 0,
                max: 4,
                grid: { display: false },
                ticks: {
                  font: {
                    weight: 'bold',
                    size: 15,
                    color: 'rgba(0,0,0,1)'
                  },
                  count: 5,
                  // minRotation: 35,
                  callback: function (label, index, labels) {
                    switch (label) {
                      case 0:
                        return ['Strongly', 'oppose']
                      case 1:
                        return 'Oppose'
                      case 2:
                        return ['Neither support', 'nor oppose']
                      case 3:
                        return 'Support'
                      case 4:
                        return ['Strongly', 'support']
                    }
                  }
                  // function(value, index, ticks) {
                  // if (yticks.includes(value)) {
                  // return value;
                  // }
                  // },
                  // tickWidth: 100,
                  // tickLength
                  // lineWidth:
                }
              },
              x: {
                grid: { display: false },
                type: 'time',
                time: {
                  unit: 'month'
                },
                ticks: {
                  // minRotation: 15,
                  font: {
                    weight: 'bold',
                    size: 15,
                    color: 'rgba(0,0,0,1)'
                  }
                }
              }
            },
            plugins: {
              title: {
                display: true,
                text: 'Support for...',
                font: { size: 30, weight: 'bold' }
              },
              legend: {
                display: false,
                position: 'right',
                labels: {
                  font: {
                    size: 22,
                    weight: 'bold'
                  }
                }
              }
            }
          }
        })

      btns = document.getElementsByClassName('demnormline-btn')
      btns[0].style.backgroundColor = 'rgba(0,0,0,.7)'
      btns[0].style.color = 'rgba(255,255,255,.9)'

      for (let i = 0; i < btns.length; i++) {
        btns[i].onclick = function () {
          // Turn off other buttons
          for (let ii = 0; ii < btns.length; ii++) {
            btns[ii].style.color = 'rgba(0,0,0,.7)'
            btns[ii].style.backgroundColor = 'rgba(0,0,0,0)'
          }
          chart.data.datasets.forEach(function (ds) {
            ds.hidden = true
          })

          // Toggle this button
          ds = chart.data.datasets[this.dataset.index]
          ds.hidden = !ds.hidden
          chart.update()

          this.style.backgroundColor = 'rgba(0,0,0,.7)'
          this.style.color = 'rgba(255,255,255,.9)'
          // this.style.backgroundColor = ['red','blue'][+ ds.hidden]
        }
      }
    })
}

build()
