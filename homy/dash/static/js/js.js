let quantity = document.querySelector('.quantity')
let increment = document.getElementsByClassName("increment");
let descremint = document.getElementsByClassName("decrement");
let insaidCart = document.getElementById('insaidCart')
let dishName = document.getElementById('dishName')




if (!window.localStorage.getItem('quantityChange')) {
  window.localStorage.setItem('quantityChange', 0);
}
if(!window.localStorage.getItem('cart')){
  window.localStorage.setItem('cart', JSON.stringify([]));
}
let quantityChange = parseInt(window.localStorage.getItem('quantityChange')) || 0;

if (quantity) {
  quantity.innerText = quantityChange;
}

let cart = JSON.parse(window.localStorage.getItem('cart')) || [];

if(insaidCart){
  
  if(cart && cart.length > 0){
    cart.forEach(item => {
      insaidCart.innerHTML += `<p>${item.name}: ${item.quantity}</p>`;
    });
  }else{
    insaidCart.innerText = "There is nothing in your cart";
  }
}

function addItem(x){
  if(x.className == 'increment'){
    quantityChange += 1
    window.localStorage.setItem('quantityChange', quantityChange);
    window.localStorage.setItem(dishName.innerText , quantityChange)
  }else if(x.className == "decrement"){
    if(quantityChange > 0){
      quantityChange -= 1
      window.localStorage.setItem('quantityChange', quantityChange);
      window.localStorage.setItem(dishName.innerText , quantityChange)
      if (quantityChange == 0){
        window.localStorage.setItem('quantityChange', quantityChange);
        window.localStorage.removeItem(dishName.innerText , quantityChange)
      }
    }
  }
  quantity.innerHTML = quantityChange
}




function addToCart(){


  // Check if the dish is already in the cart
  const existingDish = cart.find(item => item.name === dishName.innerText);

  if (existingDish) {
    // If the dish is found, update the quantity
    existingDish.quantity += quantityChange;
  } else {
    // If the dish is not found, add it to the cart
    cart.push({ name: dishName.innerText, quantity: quantityChange });
  }

  // Save the updated cart back to localStorage
  window.localStorage.setItem('cart', JSON.stringify(cart));
 
  displayCartItems(cart);
 

}



function displayCartItems(cart) {
  // Get the `insaidCart` element
  const insaidCart = document.getElementById('insaidCart');

  // Ensure `insaidCart` exists to avoid errors
  if (!insaidCart) return;

  // Clear the current contents
  insaidCart.innerHTML = '';

  // Iterate over the cart items and display each item
  cart.forEach(item => {
    insaidCart.innerHTML += `<p>${item.name}: ${item.quantity}</p>`;
  });
}


function clearCart(){
  window.localStorage.removeItem('cart')
  if (insaidCart) {
    // Update the cart display message directly
    insaidCart.innerText = "There is nothing in your cart";
}
}