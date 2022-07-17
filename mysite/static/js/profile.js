const content = document.querySelector('.content')

function changBg() {
    document.body.style.backgroundImage ="linear-gradient(-45deg, #e2a9e5 15%, #2b94e5 100%)";
}

const render = (user) => {
    content.innerHTML = `
        <div onmouseover="changBg()" id="main">
            <div id="container">
                <div class="personal">
                    <div class="img-profile">
                        <img src="/static/img/avt_${user["gender"] == 'Nam' ? 'boy' : 'girl'}.png" alt="avatar">
                    </div>
                    <div class="per-data">
                        <div class="per-title name">Họ và tên: ${user["name"]}</div>
                        <div class="per-title year-old">Tuổi: ${user["age"]}</div>
                        <div class="per-title dob">Ngày sinh: ${user["birthday"]}</div>
                        <div class="per-title sex">Giới tính: ${user["gender"]}</div>
                    </div>
                </div>
                
                <div class="data">
                    <div class="decoration">
                        <div class="box"></div>
                        <div class="box"></div>
                        <div class="box"></div>
                    </div>
                    <div class="genaral">
                        <h1>Tổng quan</h1>
                        <div class="stand-data">
                            <div class="box-title height">Chiều cao ${user["height"]}cm</div>
                            <div class="box-title weight">Cân nặng ${user["weight"]}kg</div>
                            <div class="box-title bmi">BMI <br>${user["bmi"]}</div>
                            <div class="box-title blood">Nhóm máu ${user["blood"]}</div>
                        </div>
                    </div>
                    <div class="med-rec">
                        <h1>Thông tin bệnh</h1>
                        <div class="post">
                            <div class="info">Covid</div>
                            <div class="date">Từ ngày 12/5/2021 - 30/5/2021</div>
                        </div>
                        <div class="post">
                            <div class="info">Bệnh X</div>
                            <div class="date">Từ ngày dd/mm/yyyy - dd/mm/yyyy</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `
}

const renderData = id => {
    localStorage.setItem('usr_id', id);
    fetch(`/get/user/${id}`)
        .then(res => res.json())
        .then(data => render(data))
}

var id = localStorage.getItem('usr_id');
if (id)
    renderData(id)
else
    document.querySelector('#user_id').addEventListener('keyup', e => {
        if (e.key == "Enter") {
            id = document.querySelector('#user_id').value;
            if (id)
                renderData(id)
        }
    })