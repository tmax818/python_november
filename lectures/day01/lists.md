# Lists
--
```py
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
```

```bash
['apple', 'banana', 'orange', 'strawberry', 'lettuce', 'cucumber', 'carrots']
```
<!-- .element: class="fragment" -->

--
```py
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
salad = 3 * vegetables
print(salad)
```

```bash
['lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots']
```
<!-- .element: class="fragment" -->

--
```py
my_list = [0,1,2,3,4,5]
```
--
```py
my_list = [0,1,2,3,4,5]
print(my_list[0])
```
## 0    <!-- .element: class="fragment" -->
--
```py
my_list = [0,1,2,3,4,5]
print(my_list[3])
```
## 3    <!-- .element: class="fragment" -->
--
```py
my_list = [0,1,2,3,4,5]
print(my_list[6])
```
`IndexError: list index out of range`    <!-- .element: class="fragment" -->
--
