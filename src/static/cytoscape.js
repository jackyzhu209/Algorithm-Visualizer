function cyto(){
    var cy = cytoscape({
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
    })

}


