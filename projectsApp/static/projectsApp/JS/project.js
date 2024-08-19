function format_dat(str_dat) {
    months = {
        0: "января",
        1: "февраля",
        2: "марта",
        3: "апреля",
        4: "мая",
        5: "июня",
        6: "июля",
        7: "августа",
        8: "сентября",
        9: "октября",
        10: "ноября",
        11: "декабря"
    };
    let dat = new Date(str_dat);
    return dat.getDate() + ' ' + months[dat.getMonth()] + ' ' + dat.getFullYear() + ' г.';
}

function checkComment(comment){
    if(comment == null){return "Нет комментария";}
    return "Комментарий";
}


const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value


const modalProjectElement = document.getElementById("modalProject");

document.getElementById("btnShowModalProject").onclick = function(){
    modalProjectElement.showModal();
}

document.getElementById("CloseModalProject").onclick = function(){
    modalProjectElement.close();
}


const modalTaskElement = document.getElementById("modalTask");

document.getElementById("btnShowModalTask").onclick = function(){
    modalTaskElement.showModal();
}

document.getElementById("CloseModalTask").onclick = function(){
    modalTaskElement.close();
}


const modalAddUserElement = document.getElementById("modalAddUser");

document.getElementById("btnShowModalAddUser").onclick = function(){
    modalAddUserElement.showModal();
}

document.getElementById("CloseModalAddUser").onclick = function(){
    modalAddUserElement.close();
}

// Навешиваем функцию на все формы
$(".getWorkForm").each(function(index, element) {
    getWork(element);
})

$(".update_is_ready").each(function(index, element) {
    update_is_ready(element);
})



//Добавление проекта
$("#addProject").submit(function(e){
    $.ajax({
        data: $(this).serialize(),
        type: 'POST',
        url:  $(this).attr('action'),
        success: function(response){
            modalProjectElement.close();
            let container = document.getElementById('projects');

            let newBtn = document.createElement('a');
            newBtn.setAttribute('class', 'a-btn project-btn');
            newBtn.setAttribute('href', response.title + '/');
            newBtn.innerHTML = response.title;

            container.append(newBtn);
        }
    });
    return false;
});


// Добавление задачи
$("#addTask").submit(function(e){
    $.ajax({
        data: $(this).serialize(),
        type: 'POST',
        url:  $(this).attr('action'),
        success: function(response){
            modalTaskElement.close();
            let addBtn = document.getElementById('btnShowModalTask')
            let parent = addBtn.parentElement;

            let newTask = document.createElement('div');
            newTask.setAttribute('class', 'task-container');
            newTask.innerHTML = `<div class="title">${response['title']}</div>
                                <div class="is-ready">Не выполнено</div>
                                <div >${checkComment(response['comment'])}</div>
                                <div> Дедлайн:${format_dat(response['deadline'])}</div>
                                <div class="worker" id="worker">
                                        Нет исполнителя
                                        <form class="getWorkForm" method="post" action="/project/Tasks/">
                                            <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}" wfd-id="id18">
                                            <input type="hidden" name="do" value="update_task_user">
                                            <input type="hidden" name="task-id" value="${response['task_id']}">
                                            <button type="submit" class="btn">Взять на исполнение</button>
                                        </form>
                                </div>`
            addBtn.parentNode.insertBefore(newTask, addBtn.nextSibling);
            getWork(newTask.getElementsByClassName('getWorkForm')[0]);
        },
        error: function (response) {
                 alert("Что-то пошло не так. Попробуйте позже.");
            }
    });
    return false;
});


//Добавление пользователя в проект
$("#addUser").submit(function(e){
    $.ajax({
        data: $(this).serialize() + '&project_id='+ document.getElementById("project_id").value,
        type: 'POST',
        url:  $(this).attr('action'),
        success: function(response){
            let p = document.createElement('p');
            p.innerHTML = response['username'];
            document.getElementById("user_in_project").append(p);
            modalAddUserElement.close();
        },
        error: function (response) {
            console.log(response);
            document.getElementById("msg-err").innerHTML = response.responseJSON['message'];
        }
    });
    return false;
});


// Функция, которая позволяет пользователю взять задачу
function getWork(element){
    $(element).submit(function(e){
        $.ajax({
            data: $(this).serialize(),
            type: 'POST',
            url:  $(this).attr('action'),
            success: function (response) {
                is_readyElement = element.parentElement.parentElement.getElementsByClassName('is-ready')[0];
                element.parentElement.innerHTML = 'Исполнитель: ' + response.user;// Изменение страницы в динамическом режиме
                console.log(is_readyElement.innerHTML)
                if(is_readyElement.innerHTML.trim() == 'Не выполнено'){
                    console.log(response)
                    is_readyElement.innerHTML =`<form method="post" action="/project/Tasks/" class="update_is_ready">
                                                <input type="hidden" name="task-id" value="${response['task_id']}">
                                                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}" wfd-id="id18">
                                                <input type="hidden" name="do" value="update_is_ready">
                                                <button type="submit">Отметить выполнение</button>
                                            </form>`
                    update_is_ready(is_readyElement.getElementsByClassName('update_is_ready')[0])
                }
            },
            error: function (response) {
                 alert("Что-то пошло не так. Попробуйте позже.");
            }
        });
        return false;
    });
}

// Обновление статуса задачи
function update_is_ready(element){
    $(element).submit(function(e){
        $.ajax({
            data: $(this).serialize(),
            type: 'POST',
            url:  $(this).attr('action'),
            success: function (response) {
                element.parentElement.innerHTML = 'Выполнено';
            },
            error: function (response) {
                 alert("Что-то пошло не так. Попробуйте позже.");
            }
        });

        return false;
    });
}
