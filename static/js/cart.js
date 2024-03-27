const updateButton = document.getElementsByClassName('update-cart')

for (i = 0; i < updateButton.length; i++){
    updateButton[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
    })
}
