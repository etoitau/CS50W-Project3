// get CSRF for ajax
function getCookie(name) {
    console.log("getCookie called");
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log("got token:");
console.log(csrftoken);

// get and compile template
var source = document.getElementById("item-template").innerHTML;
var template = Handlebars.compile(source);


// on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log("dom loaded");
    const userspan = document.getElementById('usernamespan');
    const username = userspan.dataset.username;
    console.log("username:");
    console.log(username);

    // get info from localstorage
    var cart = JSON.parse(localStorage.getItem(username));
    if (!cart) {
        cart = {
            'count': 0,
            'items': {},
        }
    }
    if(cart.count) {
        updateCartCount(cart.count)
    }
    console.log("cart:");
    console.log(cart);
     
    // build page
    populate_cart(cart);

    // add listeners for back to menu and confirm/order
    const back_button = document.getElementById("back_to_menu")
    back_button.addEventListener("click", function (event) {
        localStorage.setItem(username, JSON.stringify(cart));
        window.location.href = "menu/";
    });
    const confirm_button = document.getElementById("confirm_order")
    confirm_button.addEventListener("click", function (event) {
        confirmOrder();
    });

    // add listeners for delete item buttons
    document.querySelectorAll('.deleteitem').forEach(function(delbutton) {
        delbutton.addEventListener("click", function (event) {
            let num = delbutton.dataset.item_num;
            delete cart.item[parseInt(num)-1];
            cart.count -= 1;
            localStorage.setItem(username, JSON.stringify(cart));
            // delete from dom
            var deletediv = document.getElementById(num);
            deletediv.parentNode.removeChild(deletediv);
            updateCartCount(cart.count);
        });
    });
});


                
                        

function getMenuItem(itemid) {
    console.log("getMenuItem called with id:");
    console.log(itemid)
    return new Promise(function (resolve, reject) {
        const request = new XMLHttpRequest();
        request.open('POST', '/getmenuitem');
        request.setRequestHeader('X-CSRFToken', csrftoken)
        // callback for when request complete
        request.onload = () => {
            // extract json
            const jdata = request.responseText
            console.log("response from server:")
            console.log(jdata);
            // return result
            resolve(JSON.parse(jdata))
        }
        //send request
        request.send(itemid);
    })
}


function updateCartCount(count) {
    console.log("updateCartCount called")
    document.getElementById("cart_count").innerHTML = "(" + count.toString() + ")"
}


function populate_cart(cart) {
    console.log("populate_cart called")
    for (let i = 1; i <= cart.count; i++) {
        console.log("i: %i", i);
        console.log("item:");
        console.log(cart.items[i.toString()]);
        let id = cart.items[i.toString()].id;
        const menu_item_promise = getMenuItem(id);
        menu_item_promise.then(item => {
            var options = cart.items[i.toString()].options;
            if (!options) {
                options = null;
            }
            var htmlblock = template({
                item_num: i,
                category: item.category,
                name: item.name,
                size: item.size,
                options: options,
                price: item.price,
            });
            var div = document.createElement('div');
            div.id = i.toString();
            div.innerHTML = htmlblock;
            document.getElementById(cart_items).append(div);
        });
    }
}


function confirmOrder() {
    console.log("confirmOrder called");
    // reset cart in localstorage todo
    localStorage.removeItem(username)
    // tell server about order
    const request = new XMLHttpRequest();
    request.open('POST', '/cart');
    request.setRequestHeader('X-CSRFToken', csrftoken)
    request.send(JSON.stringify(cart));
}