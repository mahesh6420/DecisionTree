from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image  
import pydotplus
from config import OUTPUT_PNG_PATH

def save(clf, feature_cols):
    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                    filled=True, rounded=True,
                    special_characters=True,feature_names = feature_cols)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png(OUTPUT_PNG_PATH)
    Image(graph.create_png())