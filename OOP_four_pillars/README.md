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

## ***The 4 Pillars of OOP***

1. Abstraction
2. Inheritance
3. Encapsulation
4. Polymorphism

### ***1. Abstraction***

**Abstraction** *hides* the internal *implementations of a process* or *method* from the user. 
In this way, the user *knows what a function does*, but **not how it is done**.

### ***2. Inheritance***
**Inheritance** allows us to **define a class** that *inherits methods and properties from another class*.

### ***3. Encapsulation***
**Encapsulation** allows us to **enclose** something as in a capsule. By encapsulating something within our code, we are taking caution to *protect it from possible outside effects*.

### ***4. Polymorphism***
**Polymorphism** refers to the condition of *something occurring in several different forms*.
So, polymorphism refers to the *use of a single method/operator* to *represent different objects in different scenarios*.


