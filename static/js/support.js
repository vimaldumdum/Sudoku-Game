
function setValue(i, j, val){

            var ids = 9*i +j;
            var n = ids.toString();
            document.getElementById(n).setAttribute("value", val);
            document.getElementById(n).disabled = true;
}

function validateValue(id, val){
            document.getElementById(id).setAttribute("value", val);
            document.getElementById(id).disabled = true;
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
                    validateValue(id, val);
                }
            }, false);

}

