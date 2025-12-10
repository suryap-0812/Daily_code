let var_1 = "Hello, World!";
i = 0;

function greet() {
    console.log(var_1);
    i++;
    if (i == 10) return;    
    greet();
}

greet()