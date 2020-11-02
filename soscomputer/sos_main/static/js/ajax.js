let buttonSend = document.querySelector('.send')
buttonSend.addEventListener('click', function(e) {
    e.preventDefault();

    let form = document.querySelector('form')
    let formData = new FormData(form);
    console.log(form,formData);
    // let data = 
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/");
    xhr.send(formData);
    xhr.onload = () => {
        if(xhr.response=='false'){
            alert('Произошла ошибка')
        }
        else{
            alert('Спасибо скоро с вами свяжутся')
        }
        
    }

});