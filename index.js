function getvalue()
{
    let obj ={};
    let radius=document.getElementById('radius').value;
    let texture = document.getElementById('texture').value;
    let peri = document.getElementById('peri').value;
    let area = document.getElementById('area').value;
    let smooth = document.getElementById('smooth').value;
    obj.radius=radius;
    obj.texture=texture;
    obj.peri=peri;
    obj.area=area;
    obj.smooth=smooth;

    console.log("obj:", obj);
    postData('http://127.0.0.1:5000/', obj)
        .then(data => {
           
            alert("person is "+data.toFixed()+"% likely to get breast cancer")
        });
}
async function postData(url = '', data = {}) {
    console.log(data);
    const response = await fetch(url, {
        method: 'POST', 
        mode: 'cors', 
        cache: 'no-cache', 
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer', 
        body: JSON.stringify(data) 
    });
    console.log(response);
    return response.json(); 
}