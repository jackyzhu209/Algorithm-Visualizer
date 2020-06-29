function test(){
    document.getElementById("header").innerText = "passed"
    console.log("passed")
}

function cyto(){
    var cy = cytoscape({
        container: document.getElementById('cy')
    })
}

