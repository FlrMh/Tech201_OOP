#  OOP and OOP Four Pillars

Introduction to Object-oriented Programming and the 4 Pillars of OOP


- Abstraction
- Inheritance
- Encapsulation
- Polymorphism

## *Object-oriented Programming (OOP)*

**Object-oriented programming (OOP)** is a method of *structuring* a program by bundling related **properties and behaviors** into *individual objects*.

For instance, an **object** could represent a *person* with ***properties*** like a name, age, and address and ***behaviors*** such as walking, talking, breathing, and running. 

*Put another way:*
- **OOP** is an approach for *modeling* concrete, **real-world things** (like cars), as well as **relations between things** (like companies and employees/ students and teachers), etc. 
- **OOP** *models* **real-world entities** into **software objects** that have some *data associated with them* and can *perform certain functions*.

In order to be able to create an object, we need to define a **class**. So, let`s look at what classes are and how to create them. 

## *Classes*


A **class** is a *collection of objects*. 
- It contains the *blueprints* or the *prototype* from which the *objects are being created*.
- It is a logical entity that *contains attributes and methods*. 

To make things more simple, it helps to look at a **class** as a *template* that you follow to create your objects. 


![](images/2023-02-02%20(1).png)
```bash
    `class` = the built-in method that creates a class;
    "Plant" = The name we give to the class. Must be written using snake method (e.g. ThisIsHowYouDoIt).
    
    Class variable:
    `plant_kind` = variable that will store the attribute of the objects;
    "with_seeds" = the attribute of the objects that are created after this template.
    
    Class method:
    `def` = the built-in method that allows us to create a function;
    "grow" = the specific name we choose for the function that the objects will perform;
    (self) = a parameter of the function = it lets Python know that we are referring to the current class, that the function we are about to create will be specific to this class;
    `return` = what we want to see as a result of the function being performed by an object.
 ```
## *Instantiation a class*

- **Instantiating** = Making/creating an object from the class(template). 

![](images/2023-02-02%20(2).png)
```bash
class Plant:
      plant_kind = "with_seeds"
      
      def grow(self):
      return ("I'm growing!")
      
 print(Plant.plant_kind) # return "with_seeds"
 print(Plant.grow) # it will not output the return of the grow function, because we haven`t created an object to perform that action. 
 
 # BUT, if we create:
 
 plant_1 = Plant() 
 plant_2 = Plant()
 # as you can see, they are objects created by the template/class Plant.
 
 #And then:
 print(plant_1.plant_kind)
 print(plant_2.plant_kind)
 # they will both have the output "with_seeds", because they get the attribute of the class.
 
 # And if we print:
 print(plant_1.grow)
 print(plant_2.grow)
 # they will both have the output "I'm growing!", because they both perform now the function set in the class.
```
## ***The 4 Pillars of OOP***

1. Abstraction
2. Inheritance
3. Encapsulation
4. Polymorphism

### ***1. Abstraction***

**Abstraction** *hides* the internal *implementations of a process* or *method* from the user. 
In this way, the user *knows what a function does*, but **not how it is done**.


### ***2. Encapsulation***
**Encapsulation** allows us to *hide form users* things that they *don`t need to see*. By encapsulating something within our code, we are taking caution to *protect it from possible outside effects*.

!!! 
***Abstraction vs Encapsulation***:

- **Abstraction** = when you are using the methods (of creating classes, and assigning them attributes, and functions, and creating objects, and so on), you do not need to kow how it works. So, once you wrote the function, you don`t need to know how it works, as long as it works(refers to code written and ran in the same file). 
- **Encapsulation** is all about hiding the methods and functions you use(the more complex process) via another file.

### ***2. Inheritance***
**Inheritance** allows us to **define a class** that *inherits methods and properties from another class*.

### ***4. Polymorphism***
**Polymorphism** refers to the condition of *something occurring in several, different forms*.
So, polymorphism refers to the *use of a single method/operator* to *represent different objects in different scenarios*.

### Showcasing OOP and the 4 Pillars:

- Here is a diagram that showcases how OOP works:


![](images/2023-02-02%20(4).png)

### The benefits of using OOP:

1. ***Re-usability***
- It means **reusing some facilities** rather than building them again and again. This is done with the *use of a class*. We can use it ‘n’ number of times as per our need.
2. ***Data redundancy***
- One of the main benefits of OOP, due to the fact that through the *Inheritance pillar*, we can have the **same data stored multiple times in separate places**, so there are less chances of losing that data.
3. ***Code maintenance***
- This feature is more of a necessity for any programming languages. It helps users from doing re-work, as it is always *easier and more time-saving* to **maintain and modify** the existing codes by *incorporating new changes* into them, than re-writing them.
4. ***Security***
- With the use of data hiding and *abstraction mechanism*, we are **filtering out limited data to exposure**, which means we are maintaining security and providing only necessary data to view.
5. ***Better productivity***
6. ***Easy troubleshooting***
7. ***Polymorphism flexibility*** (data adaptation depending on where it is used)
8. ***Problem-solving*** (decomposed complex sizes of code into small chunks)

 
## ***The Lambda Functions***

**Lambda functions** are *anonymous* functions that *can contain only one expression*.

In Python, functions are normally created like this:
```bash
def example(a):
      # and then here, the function body
```
So, you declare them by using `def`, them you give them a name, and assign them arguments within the parenthesis. 

But sometimes, you might need a function with only one expression inside. For example a function that doubles its argument:
```bash
def double(x):
    return x * 2
```
 
This is a function that you can use, for example, with the `map` method:
```bash
def double(x):
  return x*2
  
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(double, my_list))
print(new_list) # [2, 4, 6, 8, 10, 12]
```
- This would be a good place to use a lambda function, as it can be *created exactly where you need to use it*. 
- This means using *fewer lines of code*, and you can avoid creating a named function that is only used once (and then has to be stored in memory).
- You use lambda functions when you need a small function for a short time – for example as an argument of a higher order function like map or filter.

The syntax of a lambda function is 
```bash
`lambda` "arguments": expression. 
# first, write the word lambda, then a single space
# a comma separated list of all the arguments
# followed by a colon
# and then the expression that is the body of the function.
```
- Note that you **can't give a name to lambda functions**, as they are **anonymous** (without a name) *by definition*.

A lambda function can have *as many arguments as you need to use*, but the body **must be one single expression**.

#### Best use cases for Lambda functions:
- Lambda functions are regularly used with the built-in functions :
1. `map()` (The built-in function map() takes a function as a first argument and applies it to each of the elements of its second argument, an iterable.) 
2. `filter()` (The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.)
- Key Functions:

in Python, they are higher-order functions that take a parameter `key` as a named argument. `key` receives a function that can be a lambda.
- *UI frameworks* like Tkinter, wxPython, or .NET Windows Forms with IronPython take advantage of lambda functions for mapping actions in response to UI events.


- Python Interpreter

When you’re playing with Python code in the interactive interpreter, Python lambda functions are often a blessing. It’s easy to craft a *quick one-liner function* to *explore some snippets of code* that will never see the light of day, outside of the interpreter.



