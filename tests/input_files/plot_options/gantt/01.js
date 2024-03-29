{
  connectors: {
    dashStyle: 'Solid',
    endMarker: {
        enabled: true,
        fillColor: '#cccccc',
        height: 24,
        lineWidth: 2,
        radius: 2,
        states: {
            hover: {
                enabled: true
            }
        },
        symbol: 'circle',
        width: 48
    },
    lineColor: '#ccc',
    lineWidth: 2,
    marker: {
        enabled: true,
        fillColor: '#cccccc',
        height: 24,
        lineWidth: 2,
        radius: 2,
        states: {
            hover: {
                enabled: true
            }
        },
        symbol: 'circle',
        width: 48
    },
    startMarker: {
        enabled: true,
        fillColor: '#cccccc',
        height: 24,
        lineWidth: 2,
        radius: 2,
        states: {
            hover: {
                enabled: true
            }
        },
        symbol: 'circle',
        width: 48
    }
  },
  
  groupZPadding: 4,
  partialFill: {
    fill: '#cccccc'
  },
  
  borderColor: '#ccc',
  borderRadius: 4,
  borderWidth: 2,
  centerInCategory: true,
  colorByPoint: true,
  colors: [
      '#fff',
      '#ccc',
      {
        linearGradient: {
            x1: 0.123,
            x2: 0.567,
            y1: 0.891,
            y2: 0.987
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
      },
      {
        animation: {
            defer: 5
        },
        patternOptions: {
            aspectRatio: 0.5,
            backgroundColor: '#999999',
            id: 'some_id_goes_here',
            opacity: 0.5,
            width: 120,
            x: 5,
            y: 10
        },
        patternIndex: 2
      }
  ],
  grouping: false,
  groupPadding: 6,
  maxPointWidth: 12,
  minPointLength: 12,
  pointPadding: 6,
  pointRange: 24,
  pointWidth: 12
  
}
