let forms = document.querySelectorAll("form");
forms.forEach((form)=>{
    form.addEventListener("submit", function (e) {
        e.preventDefault();

        let formData = new FormData(form);

        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/");
        xhr.send(formData);
        if (!formData.get('persRight')){
            alert('Подтвердите пользовательское соглашение')
        }
        else if(!formData.get('clientName') || !formData.get('clientPhone')){
            alert('Пожалуйста, заполните контактные данные')
        }
        else{
            xhr.onload = () => {
                if (xhr.response == "false") {
                    alert("Произошла ошибка"+xhr.response);
                } else {
                    alert(xhr.response);
                    if(form.classList.contains('form_modal')){
                        form.parentElement.style.display = 'none'
                    }
                }
            };
        };
    });
})