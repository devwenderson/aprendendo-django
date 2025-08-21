# Aprendendo javascript
## DOM - Document Object Model 

Com a manipulação do DOM é possível:
- Adicionar elementos na página
- Selecionar elementos da página
- Alterar o style dos elementos
- Adicionar eventos aos elementos
- Adicionar classes CSS nos elementos
- Escrever HTML com JavaScript
- Adicionar conteúdo dentro da página com JavaScript

Com todo esse poder, é possível adicionar lógica de programação à páginas HTML. Unindo JavaScript, CSS e HTML, é possível criar qualquer coisa. Desde interações básicas, como esconder a NavBar, até interações mais complexas, como um jogo de Xadrez.

### Acessando a DOM
```javascript
// Accessing an element by its ID
const headerElement = document.getElementById('header');

// Accessing elements by class name
const paragraphs = document.getElementsByClassName('paragraph');

// Accessing elements by tag name
const images = document.getElementsByTagName('img');
```

### Inserindo texto nos elementos
- `InnerHTML`: escreve um texto com valor de HTML
```javascript
const headerElement = document.getElementById('header');
headerElement.innerHTML = '<h1> New Header Text </h1>';
```

### Adicionando eventos
```javascript
// Accessing a button element
const myButton = document.getElementById('myButton');

// Adding a click event listener
myButton.addEventListener('click', function() {
    alert('Button Clicked!');
});
```

## Referências
- Manipulação do DOM com JS: https://www.freecodecamp.org/news/dom-manipulation-in-javascript/
- Manipulação do DOM - HandBook: https://www.freecodecamp.org/news/the-javascript-dom-manipulation-handbook/
- Introdução ao DOM: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting
- Aprenda DOM Manipulation: https://youtu.be/y17RuWkWdn8