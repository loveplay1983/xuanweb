function Person(first, last, age, year) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.year = year;
}

const myFather = new Person("John", "Doe", 39, "1983");

// adding a method to an object
myFather.name = function () {
    return this.firstName + " - " + this.lastName;
}

Person.nationality = "China";  // wrong, property cannot be added to an existing constructor, but object

myFather.nationality = "China";  // Correct

Person.prototype.nationality = "China"; // Correct with prototype

fatherName = "Name: " + myFather.name();  // method with parentheses
fatherAge = "Age: " + myFather.age;  // property without parentheses
document.getElementById("father-name").innerHTML = fatherName;
document.getElementById("father-age").innerHTML = fatherAge;


/**************************************************************************************/


// adding method to a constructor
function PersonFunc(first, last, age, year) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.year = year;
    this.info = function () {
        return "Name: " + this.firstName + " - " + this.lastName + "; Age: " + this.age;
    }
}

const myMother = new PersonFunc("Merry", "Lee", 30, "1974");

document.getElementById("mom-info").innerHTML = myMother.info();


/**************************************************************************************/
// new String()    // A new String object
// new Number()    // A new Number object
// new Boolean()   // A new Boolean object
// new Object()    // A new Object object
// new Array()     // A new Array object
// new RegExp()    // A new RegExp object
// new Function()  // A new Function object
// new Date()      // A new Date object

/**************************************************************************************/


const name = "loveplay1983";

let text = "";
for (const x of name) {
    text += x + "<br>";
}

document.getElementById("iter").innerHTML = text;


// build an iterable
myNum = {};

myNum[Symbol.iterator] = function () {
    let n = 0;
    done = false;
    return {
        next() {
            n += 10;
            if (n == 100) {
                done = true;
            }
            return {value: n, done: done};
        }
    };
}

let iterText = "";
for (const num of myNum) {
    iterText += num + "<br>";
}
document.getElementById("iter-custom").innerHTML = iterText;

/***************** async ********************************/
function disp(target) {
    document.getElementById("target").innerHTML = target;
}

function getFile(targetCallback) {
    let req = new XMLHttpRequest();
    req.onload = function () {
        if (req.status == 200) {
            targetCallback(this.responseText);
        } else {
            targetCallback("Error: " + req.status);
        }
    }
    req.open("GET", "test.html");
    req.send();
}

getFile(disp);

