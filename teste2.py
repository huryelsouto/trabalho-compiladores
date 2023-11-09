digraph finite_state_machine {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	rankdir=LR;
	node [shape = doublecircle]; 9 16 21 25 31 37 41 45 52 60 67 71 77 78 79 80 81 86 91 97 101 104 112 110 114 116 118 120 122 124 126 128 130 133;
	node [shape = circle];
	
	0 -> 1 [label = "λ"]
	0 -> 10 [label = "λ"]
	0 -> 17 [label = "λ"]
	0 -> 22 [label = "λ"]
	0 -> 26 [label = "λ"]
	0 -> 32 [label = "λ"]
	0 -> 38 [label = "λ"]
	0 -> 42 [label = "λ"]
	0 -> 46 [label = "λ"]
	0 -> 53 [label = "λ"]
	0 -> 61 [label = "λ"]
	0 -> 68 [label = "λ"]
	0 -> 72 [label = "λ"]
	0 -> 82 [label = "λ"]
	0 -> 98 [label = "λ"]
	0 -> 102 [label = "λ"]
	0 -> 105 [label = "λ"]
	0 -> 113 [label = "λ"]
	0 -> 115 [label = "λ"]
	0 -> 117 [label = "λ"]
	0 -> 119 [label = "λ"]
	0 -> 121 [label = "λ"]
	0 -> 123 [label = "λ"]
	0 -> 125 [label = "λ"]
	0 -> 127 [label = "λ"]
	0 -> 129 [label = "λ"]
	0 -> 131 [label = "λ"]
	
	1 -> 2 [label = "p"]
	2 -> 3 [label = "r"]
	3 -> 4 [label = "o"]
	4 -> 5 [label = "g"]
	5 -> 6 [label = "r"]
	6 -> 7 [label = "a"]
	7 -> 8 [label = "m"]
	8 -> 9 [label = "^letra digito _"]

	9 -> 9 [style = tapered, color = "#ffffff", label = "*"]
	9 -> 9 [style = tapered, color = "#ffffff", label = "return(program, None)"]



    10 -> 11 [label = "b"];
    11 -> 12 [label = "e"]
    12 -> 13 [label = "g"]
    13 -> 14 [label = "i"]
    14 -> 15 [label = "n"]
    15 -> 16 [label = "^letra digito _"]
    16 -> 16 [style = tapered, color = "#ffffff", label = "*"]
    16 -> 16 [style = tapered, color = "#ffffff", label = "return(begin, None)"]


	17 -> 18 [label = "e"];
	18 -> 19 [label = "n"]
	19 -> 20 [label = "d"]
	20 -> 21 [label = "^letra digito _"]
	21 -> 21 [style = tapered, color = "#ffffff", label = "*"]
	21 -> 21 [style = tapered, color = "#ffffff", label = "return(end, None)"]


    22 -> 23 [label = "i"];
    23 -> 24 [label = "f"]
    24 -> 25 [label = "^letra digito _"]
    25 -> 25 [style = tapered, color = "#ffffff", label = "*"]
    25 -> 25 [style = tapered, color = "#ffffff", label = "return(if, None)"]


	26 -> 27 [label = "e"];
	27 -> 28 [label = "l"]
	28 -> 29 [label = "s"]
	29 -> 30 [label = "e"]
	30 -> 31 [label = "^letra digito _"]
	31 -> 31 [style = tapered, color = "#ffffff", label = "*"]
	31 -> 31 [style = tapered, color = "#ffffff", label = "return(else, None)"]



    32 -> 33 [label = "t"];
    33 -> 34 [label = "h"]
    34 -> 35 [label = "e"]
    35 -> 36 [label = "n"]
    36 -> 37 [label = "^letra digito _"]
    37 -> 37 [style = tapered, color = "#ffffff", label = "*"]
    37 -> 37 [style = tapered, color = "#ffffff", label = "return(then, None)"]


	38 -> 39 [label = "linha"];
	39 -> 40 [label = "linha"];
	40 -> 41 [label = "^linha"];
	41 -> 41 [style = tapered, color = "#ffffff", label = "*"]
	
	42 -> 43 [label = "{"];
    43 -> 44 [label = "^bracket"]
    44 -> 45 [label = "}"]



	46 -> 47 [label = "w"];
	47 -> 48 [label = "h"]
	48 -> 49 [label = "i"]
	49 -> 50 [label = "l"]
	50 -> 51 [label = "e"]
	51 -> 52 [label = "^letra digito _"]
	52 -> 52 [style = tapered, color = "#ffffff", label = "*"]
	52 -> 52 [style = tapered, color = "#ffffff", label = "return(while, None)"]


    53 -> 54 [label = "r"];
    54 -> 55 [label = "e"]
    55 -> 56 [label = "p"]
    56 -> 57 [label = "e"]
    57 -> 58 [label = "a"]
    58 -> 59 [label = "t"]
    59 -> 60 [label = "^letra digito _"]
    60 -> 60 [style = tapered, color = "#ffffff", label = "*"]
    60 -> 60 [style = tapered, color = "#ffffff", label = "return(repeat, None)"]


	61 -> 62 [label = "u"];
	62 -> 63 [label = "n"]
	63 -> 64 [label = "t"]
	64 -> 65 [label = "i"]
	65 -> 66 [label = "l"]
	66 -> 67 [label = "^letra digito _"]
	67 -> 67 [style = tapered, color = "#ffffff", label = "*"]
	67 -> 67 [style = tapered, color = "#ffffff", label = "return(until, None)"]


	68 -> 69 [label = "letra"];
	69 -> 70 [label = "letra digito _"]
	70 -> 71 [label = "^letra digito _"]
	71 -> 71 [style = tapered, color = "#ffffff", label = "*"]
	71 -> 71 [style = tapered, color = "#ffffff", label = "return(id, None)"]
	
	
	72 -> 73 [label = ">"]
	72 -> 74 [label = "="]
	72 -> 75 [label = "!"]
	72 -> 76 [label = "<"]
	
	73 -> 77 [label = "^equal"]
	73 -> 78 [label = "="]
	
	75 -> 79 [label = "="]
	
	76 -> 80 [label = "="]
	76 -> 81 [label = "^equal"]
	
	74 -> 74 [style = tapered, color = "#ffffff", label = "return(EQ, None)"]
	
	77 -> 77 [style = tapered, color = "#ffffff", label = "*"]
	77 -> 77 [style = tapered, color = "#ffffff", label = "return(GT, None)"]
	
	78 -> 78 [style = tapered, color = "#ffffff", label = "return(GE, None)"]
	
	79 -> 79 [style = tapered, color = "#ffffff", label = "return(NE, None)"]
	
	80 -> 80 [style = tapered, color = "#ffffff", label = "return(LE, None)"]
	
	81 -> 81 [style = tapered, color = "#ffffff", label = "*"]
	81 -> 81 [style = tapered, color = "#ffffff", label = "return(LT, None)"]
	
	node [shape = circle, style = solid]
	
	82 -> 83 [label = "i"];
	83 -> 84 [label = "n"]
	84 -> 85 [label = "t"]
	85 -> 86 [label = "^letra digito _"]
	86 -> 86 [style = tapered, color = "#ffffff", label = "*"]
	86 -> 86 [style = tapered, color = "#ffffff", label = "return(type, int)"]

	82 -> 87 [label = "c"]
	87 -> 88 [label = "h"]
	88 -> 89 [label = "a"]
	89 -> 90 [label = "r"]
	90 -> 91 [label = "^letra digito _"]
	91 -> 91 [style = tapered, color = "#ffffff", label = "*"]
	91 -> 91 [style = tapered, color = "#ffffff", label = "return(type, char)"]

    
	82 -> 92 [label = "f"]
	92 -> 93 [label = "l"]
	93 -> 94 [label = "o"]
	94 -> 95 [label = "a"]
	95 -> 96 [label = "t"]
	96 -> 97 [label = "^letra digito _"]
	97 -> 97 [style = tapered, color = "#ffffff", label = "*"]
	97 -> 97 [style = tapered, color = "#ffffff", label = "return(type, float)"]
	
	
	98 -> 99 [label = "+ -"]
	98 -> 100 [label = "digito"]

	99 -> 100 [label = "digito"]
	100 -> 100 [label = "digito"]
	
	100 -> 101 [label = "^digito"] 
	
	101 -> 101 [style = tapered, color = "#ffffff", label = "*"]
	101 -> 101 [style = tapered, color = "#ffffff", label = "return(constant_int, None)"]
	
    node [shape = circle, style = solid]
    102 -> 103 [label = "'"];
	103 -> 103 [label = "letra digito"]
	103 -> 104 [label = "'"]
	104 -> 104 [style = tapered, color = "#ffffff", label = "*"]
	104 -> 104 [style = tapered, color = "#ffffff", label = "return(constant_char, None)"]



	105 -> 106 [label = "digito"];
	106 -> 106 [label = "digito"];
	106 -> 107 [label = "."];
	106 -> 109 [label = "fracao"];
	107 -> 108 [label = "digito"];
	108 -> 109 [label = "fracao"];
	108 -> 108 [label = "digito"];
	108 -> 112 [label = "^digito.fracao"];
	109 -> 109 [label = "+ -"];
	109 -> 110 [label = "digito"];
	110 -> 110 [label = "digito"];

    
	112 -> 112 [style = tapered, color = "#ffffff", label = "*"]
	112 -> 112 [style = tapered, color = "#ffffff", label = "return(constant_float, None)"]
	110 -> 110 [style = tapered, color = "#ffffff", label = "*"]
	110 -> 110 [style = tapered, color = "#ffffff", label = "return(constant_exp, None)"]



	113 -> 114 [label = "("];
	114 -> 114 [style = tapered, color = "#ffffff", label = "*"]

	114 -> 114 [style = tapered, color = "#ffffff", label = "return(left_parent, None)"]
	
    node [shape = circle, style = solid];
	115 -> 116 [label = ")"];
	116 -> 116 [style = tapered, color = "#ffffff", label = "*"]
	116 -> 116 [style = tapered, color = "#ffffff", label = "return(right_parent, None)"]



    node [shape = circle, style = solid];
	117 -> 118 [label = ";"];
	118 -> 118 [style = tapered, color = "#ffffff", label = "*"]
	118 -> 118 [style = tapered, color = "#ffffff", label = "return(;, None)"]


    node [shape = circle, style = solid];
	119 -> 120 [label = ":"];
	120 -> 120 [style = tapered, color = "#ffffff", label = "*"]
    node [shape = none, style = invis]; 120;
	120 -> 120 [style = tapered, color = "#ffffff", label = "return(:, None)"]

    node [shape = circle, style = solid];
	121 -> 122 [label = "+"];
	122 -> 122 [style = tapered, color = "#ffffff", label = "*"]
	122 -> 122 [style = tapered, color = "#ffffff", label = "return(+, None)"]

    node [shape = circle, style = solid];
	123 -> 124 [label = "-"];
	124 -> 124 [style = tapered, color = "#ffffff", label = "*"]
	124 -> 124 [style = tapered, color = "#ffffff", label = "return(-, None)"]

    node [shape = circle, style = solid];
	125 -> 126 [label = "*"];
	126 -> 126 [style = tapered, color = "#ffffff", label = "*"]
	126 -> 126 [style = tapered, color = "#ffffff", label = "return(*, None)"]

    node [shape = circle, style = solid];
	127 -> 128 [label = "/"];
	128 -> 128 [style = tapered, color = "#ffffff", label = "*"]
	128 -> 128 [style = tapered, color = "#ffffff", label = "return(/, None)"]

    node [shape = circle, style = solid];
	129 -> 130 [label = "^"];
	130 -> 130 [style = tapered, color = "#ffffff", label = "*"]
	130 -> 130 [style = tapered, color = "#ffffff", label = "return(^, None)"]
    
    node [shape = circle, style = solid];
	131 -> 132 [label = ":"];
	132 -> 133 [label = "="]
	133 -> 133 [style = tapered, color = "#ffffff", label = "return(:=, None)"]
}