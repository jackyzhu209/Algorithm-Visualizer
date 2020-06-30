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
        ]
    })

}


