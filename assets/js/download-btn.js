var btn = document.getElementById('download-btn-all')
btn.onclick = function () {
    window.location.href = 'https://apps.polarizationresearchlab.org/api/count/Data/Public/all_data.zip';
}

var btn = document.getElementById('download-btn-week')
btn.onclick = function () {
    var file = document.getElementById('dlselectbox').value
    window.location.href = 'https://apps.polarizationresearchlab.org/api/count/' + file;
}

var btn = document.getElementById('download-btn-week-topline')
btn.onclick = function () {
    var selectInput = document.getElementById('dlselectbox')
    var selected = selectInput.options[selectInput.selectedIndex]
    var file = 'w' + selected.dataset.week + '_' + selected.dataset.year + 'topline_engaged.pdf'
    window.location.href = 'https://dtwknrym6jvxy.cloudfront.net/' + file;
}
