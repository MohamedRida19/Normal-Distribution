<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 20px;
        }

        h1, h2, h3 {
            color: #333;
        }

        p {
            color: #666;
        }

        code {
            background-color: #f0f0f0;
            padding: 2px 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        pre {
            background-color: #f8f8f8;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
    <title>Figures Builder Program</title>
</head>
<body>

<h1>Figures Builder Program</h1>

<h2>Overview</h2>

<p>This Python program is designed to generate figures based on the normal distribution using user-defined parameters. It provides a customizable experience for users to experiment with various settings and visualize the resulting figures.</p>

<h2>Features</h2>

<ul>
    <li>Generates figures based on the normal distribution.</li>
    <li>User-friendly interface with customizable options for graph appearance.</li>
    <li>Allows users to specify the number of attempts to run the program.</li>
</ul>

<h2>Dependencies</h2>

<ul>
    <li>NumPy</li>
    <li>Seaborn</li>
    <li>Matplotlib</li>
</ul>

<h2>How to Use</h2>

<ol>
    <li>Run the program in a Python environment.</li>
    <li>Input the number of attempts to run the program.</li>
    <li>Choose whether to customize graph options for each attempt.</li>
    <li>Customize graph options such as loc (bell start), scale (graph flatness), graph color, font type, font size, and font color.</li>
    <li>View the generated figure for each attempt.</li>
    <li>Program execution finishes, displaying the message "program executing has been finished."</li>
</ol>

<h2>Default Values</h2>

<ul>
    <li><code>default_loc_var</code>: 0</li>
    <li><code>default_scale_var</code>: 1</li>
    <li><code>default_graph_color</code>: "blue"</li>
    <li><code>default_font_type</code>: "Arial"</li>
    <li><code>default_font_size</code>: 16</li>
    <li><code>default_font_color</code>: "red"</li>
</ul>

<h2>Error Handling</h2>

<p>The program handles incorrect input values and keyboard interrupts gracefully.</p>

<h2>Additional Notes</h2>

<p>This program is designed for educational purposes and allows users to explore the impact of different parameters on the normal distribution graph.</p>

</body>
</html>
