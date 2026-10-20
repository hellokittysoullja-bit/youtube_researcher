# Accessibility Insights for Windows  - Color Contrast Analyzer
Accessibility Insights · 4 мин · 9709 просмотров · en · https://youtu.be/eEAYRBG4TOE



[00:00] Welcome to Accessibility Insights, tools that make it easy for developer teams to find and fix Accessibility issues. This video introduces the  Color Contrast Analyzer in Accessibility Insights for Windows. You will learn how to manually  verify that text, UI components and graphics have sufficient contrast against the background. To launch the Color Contrast Analyzer, open Accessibility Insights for Windows, and in the navigation bar, select contrast. We'll start by testing the contrast of text 

[00:33] in a test app called Wildlife Manager. The first step is to identify any text that might have low contrast. You don't need to test any text that's part of an inactive component, purely decorative, intended to be hidden  from users, or part of a logo or brand name. The Wildlife Manager App has several potential problems with low contrast. We'll test the text in this close button. It's medium blue text on a light blue background. 

[01:04] First, turn off auto detect. Next, under Color 1 select the foreground color of the text. Select the eyedropper, use the mouse to hover over the text. Use the arrow keys to nudge the pointer pointer to a specific pixel, and then press the enter key. Under Color 2 select the text  background color. Select the eyedropper and select a pixel. The Color Contrast Analyzer shows that this text fails the contrast requirements for text of any size. 

[01:34] Now we'll test the contrast of some UI components. The first step is to identify any UI components, whose boundaries or state indicators might be low contrast in any of these states. Normal, mouse over, focused, or selected. You won't need to test any UI components that are inactive or that user browser's default appearance. Let's take a look at the current animals grid. The headers in this grid are interactive UI Components 

[02:04] Their boundaries are indicated by a border. The border between the two headers appears to have low contrast in normal state so that warrants testing. The headers change color on Mouseover, so we'll test that same border in Mouseover state too. The headers can't be focused or selected. So we don't need to test those states. First, we'll test the border contrast in the normal normal state. Under color 1 select pixel in the border and under color 2 select an adjacent pixel. 

[02:35] The Color Contrast Analyzer shows that the boundary fails, the contrast requirement for UI components. Next we'll test the border contrast in Mouseover State. For that we'll need to get a screenshot of the component. Launch Snip n Sketch. Under New select Snip in 3 seconds Hover your mouse over the first header, wait for the 3 seconds to pass, and then grab a screenshot. Now we'll test the contrast using the screenshot. Again under color 1, select a pixel in the border. 

[03:06] And under color 2, selecting adjacent pixel. The boundary contrast fails in Mouseover State, too. Finally we'll test the contrast of a graphical object in this Excel spreadsheet. Graphics include icons, charts, diagrams, and illustrations. The first step is to identify any graphics that might have low contrast elements. You don't need to test any graphic where a particular presentation is essential. And presenting it with sufficient contrast would undermine its meaning. 

[03:37] Logos, photos of real life scenes, illustrations using realistic colors, and screenshots are all exempt from the contrast requirement. And you don't need to test a graphic if it's purely decorative, or if the information conveyed by the graphic is also conveyed through visible text. So we can ignore this owl icon and focus on the pie chart. It's divided into 4 unequal slices each labeled with the person's name. First, we need to identify the parts that must be visible 

[04:08] for the graphic to be understood. In this case, the necessary parts are the slices, because they communicate the proportion, associated with each person. We'll test whether each slice has sufficient contrast against the white background? Under color 1 select a pixel in this yellow slice, labeled Sally. Under color 2 select the white background. The yellow slice fails, and so does the Gray and the orange? Only the Blue slice passes. 

[04:38] That concludes the demo. For more information about Accessibility Insights for Windows Windows visit accessibilityinsight.io 
