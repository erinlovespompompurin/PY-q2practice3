from pyscript import document, display

def checkNum(e) :

    num_bers= ["7", "8", "10", "19", "90"]

    num1= document.getElementById("num1").value
    name= "Kendall"

    confirm_num = num1() in num_bers

    message = (f'Sorry{name}, your number is not found.' , f'Yey! {name}, Your number is found.')

    document.getElementById("output1").innerHTML = message[confirm_num]