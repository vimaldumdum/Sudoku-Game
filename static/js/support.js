var solved;
function setValue(i, j, val){

            var ids = 9*i +j;
            var n = ids.toString();
            document.getElementById(n).setAttribute("value", val);
            document.getElementById(n).disabled = true;
}

function validateValue(i, j, val){
            var id = 9*i +j;
            id = id.toString();
            if(solved[i][j] === val){
                document.getElementById(id).setAttribute("value", val);
                document.getElementById(id).disabled = true;
            }
            else{
                document.getElementById(id).style.backgroundColor = "red";
                document.getElementById(id).value = "";
                setTimeout(function(){
                document.getElementById(id).style.backgroundColor = "lightgreen";}, 1000)
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

function getSolved(sol){
    solved = sol;
}

