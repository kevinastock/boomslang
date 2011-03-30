from Location import Location

class Legend(object):        
    def __init__(self, columns = 1, scatterPoints = 3, drawFrame = True,
                 location = "best", figLegend = False, labelSize = None):
        self._loc = Location()
        self.labelSize = labelSize
        self.columns = columns
        self.scatterPoints = scatterPoints
        self.drawFrame = drawFrame
        self.location = location
        self.figLegend = figLegend
        
    @property
    def location(self):
        return self._loc.location

    @location.setter
    def location(self, value):
        self._loc.location = value
    
    def _genLegendKeywords(self, axes, handles, labels):
        legendKeywords = {}
        
        if self.columns > 1:
            versionParts = [int(x) for x in matplotlib.__version__.split('.')]
            
            (superMajor, major, minor) = versionParts[0:3]
            
            if superMajor == 0 and major < 98:
                print >>sys.stderr, "Number of columns support not available "\
                    "in versions of matplotlib prior to 0.98"
            else:
                legendKeywords["ncol"] = self.legendCols
                legendKeywords["scatterpoints"] = self.scatterPoints
                
        if self.labelSize is not None:
            legendKeywords["prop"] = {"size" : self.labelSize}
            
        return legendKeywords
    
    def _formatLegend(self, axes, legend):
        if legend:
            legend.draw_frame(self.drawFrame)

    def draw(self, figure, handles, labels):
        if not self.figLegend:
            raise Exception("This draw() method should only be called on "
                            "figure legends")
        
            
    def draw(self, axes, handles, labels):
        if self.figLegend:
            raise Exception("This draw() method shouldn't be called on "
                            "figure legends")
        
        legendKeywords = self._genLegendKeywords(axes, handles, labels)
        
        legend = None
        
        if len(handles) > 0:
            legend = axes.legend(handles, labels, loc=self.location,
                                 **legendKeywords)
        
        if legend:
            legend.draw_frame(self.drawFrame)