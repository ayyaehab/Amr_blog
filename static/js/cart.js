
var updateBtns = document.getElementsByClassName('update-cart')
// var close = document.getElementsByClassName('close')
// for (i = 0; i < close.length; i++) {
// 	close[i].addEventListener('click', function(){
// 	var productId = this.dataset.product
// 	console.log('productIdfromclose:', productId)
// 	delete cart[productId];
// 	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
// 	location.reload()
// })
// }
for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		// console.log('productId:', productId, 'Action:', action)
        addCookieItem(productId, action)
	})
}


function addCookieItem(productId, action){
	// console.log('User is not authenticated')
	console.log('productId:', productId, 'Action:', action)
	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			// console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	if (action == 'close'){
			delete cart[productId];
		
	}
	// console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}