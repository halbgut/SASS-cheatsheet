# SASS Cheatsheet
##Syntax
### Declarations
	border: 1px solid tomato
	:border 1px solid tomato

### Imports
	@import components/code

### Mixins
#### Defining Mixins
	=bounce ($param1, $param2)
		<Your mixin here>

#### Calling Mixins
	+bounce (yolo, swag)

### Defining Maps and Lists
	$var-map: ( value: 1, price: 2 )
	$var-list: yolo, zolo, molo, tolo
**Invalid:**
	$var-map: (
		guess: 23,
		answer: 42
	)
Note: Same goes for lists
This is awful but:
> Planned - /issues/216 - 13 Aug 14

### Shorthand properties #UNDOCUMENTED
	font:
		family: "Comic Sans", Arial
		size: 2em

### Variable defaults
	$answer-to-question || No!