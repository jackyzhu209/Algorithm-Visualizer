var cy;

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
    var elabel = document.getElementById('E');
    var esource = document.getElementById('S');
    var etarget = document.getElementById('T');

    var json = JSON.stringify({"Type": "E", "data": {"id": elabel.value, "source": esource.value, "target": etarget.value}});

    cy.add({group: 'edges', data: {id: elabel.value, source: esource.value, target: etarget.value}});

    elabel.value = "";
    esource.value = "";
    etarget.value = "";

    var xhttps = new XMLHttpRequest()
    xhttps.open("POST", '/updateGraph');
    xhttps.send(json)
}

function addvertex(){
    var vlabel = document.getElementById('V');

    var json = JSON.stringify({"Type": "V", "data": {"id": vlabel.value}});

    console.log(json);

    cy.add({group: "nodes", data: {id: vlabel.value}});

    vlabel.value = "";

    var xhttps = new XMLHttpRequest();
    xhttps.open("POST", "/updateGraph");
    xhttps.send(json)
}


