var items = document.getElementsByClassName("home-card-box")
for (var i = 0; i < items.length; i++) {
    items.item(i).onclick = function () {
        window.location.href = this.dataset.destination
    }
}