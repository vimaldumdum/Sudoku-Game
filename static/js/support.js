var solved;
var gameOver = false;
var lost = false;
var sec = 0;
var total;

function pad ( val ) { return val > 9 ? val : "0" + val; }
    setInterval( function(){
        if(total != 0){
            document.getElementById("seconds").innerHTML=pad(++sec%60);
            document.getElementById("minutes").innerHTML=pad(parseInt(sec/60,10));
        }
    }, 1000);
function setValue(i, j, val){

            var ids = 9*i +j;
            var n = ids.toString();
            document.getElementById(n).setAttribute("value", val);
            document.getElementById(n).style.color = "#000000";
            document.getElementById(n).disabled = true;

}

function validateValue(i, j, val){
            var id = 9*i +j;
            id = id.toString();
            if(solved[i][j] === val){
                document.getElementById(id).setAttribute("value", val);
                document.getElementById(id).style.color = "#000000";
                document.getElementById(id).disabled = true;
                total = total-1;
                console.log(total.toString());
                if(total == 0)
                {
                    gameOver = true;
                    lost = false;
                    endGame(lost);
                }
            }
            else{
                document.getElementById(id).style.backgroundColor = "red";
                document.getElementById(id).value = "";
                setTimeout(function(){
                document.getElementById(id).style.backgroundColor = "transparent";}, 500);

            }
}

function fillValues(grid){
    for(i=0;i<9;i++){
        for(j=0;j<9;j++){
            if(grid[i][j]!=0)
                setValue(i,j, grid[i][j])
        }
    }
}

function clickFun(id){

         document.getElementById(id).addEventListener('keypress', function (e) {
                if (e.keyCode === 13) {
                    var val = document.getElementById(id).value;
                    var num = parseInt(id);
                    var j = num%9;
                    num = num - j;
                    var i = num/9;
                    validateValue(i, j, parseInt(val));
                }
            }, false);

}

function getSolved(sol, miss){
    solved = sol;
    total = miss;
    console.log('total found');
    console.log(total);
}

function solve(id){
    var num = parseInt(id);
    var j = num%9;
    num = num - j;
    var i = num/9;

    document.getElementById(id).setAttribute("value", solved[i][j]);
    document.getElementById(id).style.color = "#000000";
    document.getElementById(id).disabled = true;

}

function solveFull(){
    document.getElementById("b1").disabled = true;
    total = 0;
    for(i=0;i<81;i++){
        var id =i.toString();
        if(document.getElementById(id).disabled == false){
            solve(id);
        }
    }
    gameOver = true;
    lost = true;

    endGame(lost);

}

function endGame(lost){

    var modal = document.getElementById("simpleModal");
    var closeButton = document.getElementById("closeBtn");
    console.log('working');
    if(lost == true)
        document.getElementById('modalText').innerHTML = "You Lost";
    else{
        var sec = document.getElementById('seconds').innerHTML;
        var min = document.getElementById('minutes').innerHTML;
        document.getElementById('modalText').innerHTML = "You Won in " + min.toString() + "minutes and "+sec.toString()+"seconds";
    }
    modal.style.display = 'block';

    closeButton.addEventListener("click", function(){
        modal.style.display = 'none';
    });
}

