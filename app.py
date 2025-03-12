from flask import Flask, render_template, request
import random

app = Flask(__name__)

class FashionDesignAI:
    def __init__(self):
        self.body_sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
        self.styles = ['Casual', 'Formal', 'Party', 'Business', 'Sporty']
        self.colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow']
        self.fabrics = ['Cotton', 'Silk', 'Denim', 'Leather', 'Linen']
        self.dresses = []  # List to store dress designs
        
    def describe_outfit(self, size):
        if size not in self.body_sizes:
            return "Size not available."
        description = f"Selected size: {size}. The outfit is designed to fit body dimensions of {self.get_size_description(size)}."
        return description
    
    def get_size_description(self, size):
        size_descriptions = {
            'XS': 'Chest: 30-32 inches, Waist: 24-26 inches, Hips: 32-34 inches',
            'S': 'Chest: 32-34 inches, Waist: 26-28 inches, Hips: 34-36 inches',
            'M': 'Chest: 34-36 inches, Waist: 28-30 inches, Hips: 36-38 inches',
            'L': 'Chest: 36-38 inches, Waist: 30-32 inches, Hips: 38-40 inches',
            'XL': 'Chest: 38-40 inches, Waist: 32-34 inches, Hips: 40-42 inches',
            'XXL': 'Chest: 40-42 inches, Waist: 34-36 inches, Hips: 42-44 inches'
        }
        return size_descriptions.get(size, "Size not available.")
    
    def generate_design(self, style, color, fabric):
        if style not in self.styles or color not in self.colors or fabric not in self.fabrics:
            return "Invalid input. Please select from the available styles, colors, and fabrics."
        
        design = {
            'Style': style,
            'Color': color,
            'Fabric': fabric,
            'Description': f"Stylish {style} dress in {color} color made of {fabric} fabric."
        }
        self.dresses.append(design)
        return design
    
    def modify_design(self, design_index, style=None, color=None, fabric=None):
        if design_index >= len(self.dresses):
            return "Design index not found."
        
        design = self.dresses[design_index]
        
        if style:
            design['Style'] = style
        if color:
            design['Color'] = color
        if fabric:
            design['Fabric'] = fabric
        
        design['Description'] = f"Stylish {design['Style']} dress in {design['Color']} color made of {design['Fabric']} fabric."
        return design
    
    def create_collection(self, num_designs=5):
        collection = []
        for _ in range(num_designs):
            style = random.choice(self.styles)
            color = random.choice(self.colors)
            fabric = random.choice(self.fabrics)
            design = self.generate_design(style, color, fabric)
            collection.append(design)
        return collection

fashion_ai = FashionDesignAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/describe_outfit', methods=['POST'])
def describe_outfit():
    size = request.form['size']
    description = fashion_ai.describe_outfit(size)
    return render_template('index.html', description=description)

@app.route('/generate_design', methods=['POST'])
def generate_design():
    style = request.form['style']
    color = request.form['color']
    fabric = request.form['fabric']
    design = fashion_ai.generate_design(style, color, fabric)
    return render_template('index.html', design=design)

@app.route('/modify_design', methods=['POST'])
def modify_design():
    design_index = int(request.form['design_index'])
    style = request.form['style']
    color = request.form['color']
    fabric = request.form['fabric']
    modified_design = fashion_ai.modify_design(design_index, style, color, fabric)
    return render_template('index.html', modified_design=modified_design)

@app.route('/create_collection', methods=['POST'])
def create_collection():
    collection = fashion_ai.create_collection(3)
    return render_template('index.html', collection=collection)

if __name__ == '__main__':
    app.run(debug=True)
  
