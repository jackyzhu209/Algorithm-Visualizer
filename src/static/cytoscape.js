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
                    data: {id: 'a-b', source: 'a', target: 'b'},
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
                    'label': 'data(id)'
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
                cy.add({group: 'edges', data: {id: esource.value + "-" + etarget.value, source: esource.value, target: etarget.value, weight: elabel.value}});

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
                document.getElementById("error").innerText = ""
            }
        }
    };
    xhttps.open("POST", "/updateGraph");
    xhttps.send(json);
}


