# Illustrator Scripting

With Illustrator Scripting you can create code-generated drawings, or you can write your own tools to streamline your workflow in Illustrator.

## Documentation

Adobe publishes two PDFs for documentation:

- The Adobe Illustrator **Scripting Guide**
- The Adobe Illustrator **Javascript Reference**

Go to the download page at [Illustrator Scripting Documentation - Adobe Developer Connection](http://www.adobe.com/devnet/illustrator/scripting.html) and get these two documents for your version of Illustrator.

- The **Scripting Guide** will explain you the basics of setting up your scripting toolchain, and will explain the DOM (Document-Object-Model) used by Illustrator
- The **Javascript Reference** contains a detailed list of all the functions and methods you can call on Illustrator and its objects. And it contains a lot of example code demonstrating how to use these functions.

![Illustrator's Document Object Model]()

## Apps to use

If you're writing your script and debugging it, you'll be running a few apps next to each other:

- ExtendScript Toolkit
- Illustrator (this is the target app)
- Your favorite text editor (e.g. Sublime text)
- Console (in Utilities)

## Language

- Javascript (not python)

While Adobe supports a few languages for scripting (AppleScript, VBScript and Javascript), it doesn't support Python unfortunately. We choose **Javascript** because because support by Adobe is better and it can be applied more universal.

## Using this

So how to go about using this?

As an example of a script, let's set all *Path Items* in a document to a random color. The code for this can be found in the **Reference** under "*Setting colors in a path*":

```javascript
// Sets the stroke and fill of a path item to colors of a randomly selected swatch

if ( app.documents.length > 0 && app.activeDocument.pathItems.length > 0 ) {
    doc = app.activeDocument;
    for (var i = 0; i < doc.pathItems.length; i++ ) {
        pathRef = doc.pathItems[i];
        pathRef.filled = true;
        pathRef.stroked = true;
        swatchIndex = Math.round( Math.random() * ( doc.swatches.length - 1 ) );
        pathRef.fillColor = doc.swatches[ swatchIndex ].color;
        pathRef.strokeColor = doc.swatches[ swatchIndex ].color;
    }
}
```

### 1. Where to install

### 2. How to use

### 3. How to automate

## Cases to use Illustrator Scripting over Plotdevice.io?

Why would you use Illustrator Scripting and not draw the stuff in python / Plotdevice? That's a good question. Most of the stuff you can do in Illustrator, you can also do in Plotdevice. So if you want to draw this stuff using code, often Plotdevice (or Processing for that matter), would be easier because you can stay in one application, and use a language you're familiar with.

However, there are some use cases in which Illustratot offers you functionality, you can not get from Plotdevice or Processing. I've identified a few of these use cases:

- Drawing stuff "by hand" using the *pen tool*
- Path functions like *Outline*
- Distort and Transform functions like *Twist* or *ZigZag*

----

