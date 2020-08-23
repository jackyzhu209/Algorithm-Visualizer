var cy;

function newGraph(){
    var https = new XMLHttpRequest();
    https.open("POST", "/newGraph");
    https.send();
}
function cyto(){
    cy = cytoscape({
        container: document.getElementById('cy'),
        elements: {
            nodes: [
                {
                    data: {id: 'a'},
                    position: {x:100, y:100}
                },
                {
                    data: {id: 'b'},
                    position: {x:200, y:200}
                }
            ],
            edges: [
                {
                    data: {id: 'a-b', source: 'a', target: 'b', weight: 1},
                },
                {
                    data: {id: 'b-a', source: 'b', target: 'a', weight: 1}
                }
            ]
        },
        layout: {
            name: 'grid',
            rows: 1
        },
        style: [
            {
                selector: 'node',
                style: {
                    'label': 'data(id)',
                    'color' : 'white',
                    'background-color': 'blue'
                }
            },
            {
                selector: 'edge',
                style: {
                    'label': 'data(weight)',
                    'color' : 'white',
                    'line-color': 'blue'
                }
            }
        ],
        wheelSensitivity: 0.1,
        panningEnabled: true
    });


}

function addedge(){
    var elabel = document.getElementById('W');
    var esource = document.getElementById('S');
    var etarget = document.getElementById('T');

    var json = JSON.stringify({"Type": "E", "data": {"id": elabel.value, "source": esource.value, "target": etarget.value}});

    var xhttps = new XMLHttpRequest();
    xhttps.onreadystatechange = function(){
        if(this.readyState === 4){
            if(this.responseText !== "Pass"){
                document.getElementById("error").innerText = this.responseText
            }
            else{
                cy.add({group: 'edges', data: {id: esource.value + "-" + etarget.value, source: esource.value, target: etarget.value, weight: parseInt(elabel.value)}});
                cy.add({group: 'edges', data: {id: etarget.value + "-" + esource.value, source: etarget.value, target: esource.value, weight: parseInt(elabel.value)}});
                elabel.value = "";
                esource.value = "";
                etarget.value = "";
                document.getElementById("error").innerText = "";
            }
        }
    };
    xhttps.open("POST", '/updateGraph');
    xhttps.send(json)
}

function addvertex(){
    var vlabel = document.getElementById('V');

    var json = JSON.stringify({"Type": "V", "data": {"id": vlabel.value}});

    console.log(json);

    var xhttps = new XMLHttpRequest();
    xhttps.onreadystatechange = function(){
        if(this.readyState === 4){
            if(this.responseText !== "Pass"){
                document.getElementById("error").innerText = this.responseText
            }
            else{
                cy.add({group: "nodes", data: {id: vlabel.value}});
                vlabel.value = "";
                document.getElementById("error").innerText = "";
            }
        }
    };
    xhttps.open("POST", "/updateGraph");
    xhttps.send(json);
}

function runAlgo(){
    var selectedAlgo = document.getElementById("Algorithm").value;
    var start = document.getElementById("startNode").value;
    var end = document.getElementById("endNode").value;
    var json = JSON.stringify({"Algo": selectedAlgo, "Start": start, "End": end});
    console.log(json);
    var xhttps = new XMLHttpRequest();

    xhttps.onreadystatechange = function(){
        var parsed = JSON.parse(this.responseText)["result"];
            if(this.readyState === 4){
                if(typeof parsed == "string"){
                    document.getElementById("Connectivity").innerText = "";
                    document.getElementById("Path").innerText = "";
                    if(parsed === "not connected"){
                        document.getElementById("Connectivity").innerText = parsed
                    }
                    else{
                        document.getElementById("error").innerText = this.responseText;
                    }
                }
                else{
                    console.log(parsed)
                    document.getElementById("Path").innerText = "";
                    cy.edges().style('line-color', 'blue');
                    for(var node = 1; node < parsed.length; node ++){
                        var id = "#"+parsed[node-1].toString() + "-" + parsed[node].toString();
                        var id2 = "#"+parsed[node].toString() + "-" + parsed[node-1].toString();
                        cy.$(id).style('line-color', 'red')
                        cy.$(id2).style('line-color', 'red')
                    }
                    document.getElementById("Connectivity").innerText = "connected";
                    document.getElementById("Path").innerText = parsed.toString();
                    document.getElementById("startNode").value = "";
                    document.getElementById("endNode").value = "";
                    document.getElementById("error").innerText = "";
                }
            }
        };
    xhttps.open("POST", '/runAlgo');
    xhttps.send(json);

    document.getElementById("startNode").value = "";
    document.getElementById("endNode").value = "";
}