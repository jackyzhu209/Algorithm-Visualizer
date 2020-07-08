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

    var json = JSON.stringify({"Type": "E", "data": {"label": elabel.innerText, "source": esource.innerText, "target": etarget.innerText}})

    cy.add({group: 'edges', data: {id: JSON.stringify(elabel.innerText), source: JSON.stringify(esource.innerText), target: JSON.stringify(etarget.innerText)}});

    elabel.innerText = "";
    esource.innerText = "";
    etarget.innerText = "";

    return json
}

function addvertex(){

}


