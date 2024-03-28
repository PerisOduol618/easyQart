// Iterate through all elements with class 'update-cart'
const updateButton = document.getElementsByClassName('update-cart')

for (i = 0; i < updateButton.length; i++){
    updateButton[i].addEventListener('click', function(){
        // Get product ID and action from data attributes
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('user is not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

// Add event listener to each element
function updateUserOrder(productId,action){
    console.log('user is logged in, sending data ...')

    // this is where the fetched data is sent
    const url = '/update_Item/'

    // send the post data to the backend 
    fetch(url, {
        method:'POST',
        headers:{
            'content-type':"application/json",
            'X-CSRFToken':csrftoken,

        },
        // send the object to the backend as a string
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    // return/get the updateItem response as a promise to fetch turn it to json value
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
    })
}