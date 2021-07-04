// Reading from config for paths
var config = new Object();
config["leetcode_path"] = "/Users/derekthomas/projects/LeetCode/leetcode/editor/en/";

// Calculate paths
let python_file_name = await tp.system.clipboard();
let md_file_name = python_file_name.replace(".py", ".md");
let python_path = config["leetcode_path"] + python_file_name;
let md_path = config["leetcode_path"] + md_file_name;

// Rename Obsidian filename
let ob_file_name = python_file_name.replace(".py", "").replace('[', '').replace(']', ' - ');
tp.file.rename(ob_file_name);

// Read files
function get_text(path) {
    const fs = require('fs');

    try {
        const data = fs.readFileSync(path, 'utf8');
        return data
    } catch (err) {
        console.error(err);
    }
}

var original = get_text(python_path);
var md = get_text(md_path);

// Process python file
let mdSplitIndex = original.indexOf('\n\n');
let end_split_index = original.indexOf('\n# Success:');

let code = original.slice(mdSplitIndex,end_split_index);
let end = original.slice(end_split_index,original.length);

let code_before = "\n# Code\n```py";
let code_after = "```\n";
let end_cleanup = end.replaceAll("# ", '');

function get_regex(regex, input_str) {
    input_match = [...input_str.matchAll(regex)];
    return input_match[0][1];
}

// Parse html topics
const topics_re = /<div><div>Related Topics<\/div><div>.+<\/div><\/div>/g;
topic_match = [...md.matchAll(topics_re)];
var parser = new DOMParser();
var parsedHtml = parser.parseFromString(topic_match[0][0], "text/html");

let liTags = parsedHtml.getElementsByTagName("li");
let tags = []

for (let item of liTags) {
    console.log(item.textContent);
    tags.push(item.textContent.replaceAll(" ", "_"));
}


// Regexs for vars
const runtime_re = /Runtime:(\d+ ms)/g
const faster_re = /faster than ([^ ]+)/g
const memory_re = /Memory Usage:(.+?),/g
const less_re = /less than ([^ ]+)/g
const time_re = /Time:: (.+)/g

// Optional regex
try{
    var total_time = get_regex(time_re, end_cleanup);
}catch(error){
    var total_time='';
}

// Outputting to file
tR += `---\n`;
tR += `tags: ${tags}\n`
tR += `fileType: LeetCode\n`;
tR += `creationDate: ${tp.date.now('YYYY-MM-DD')} \n`;
tR += `---\n`;
tR += `${md}\n`;
tR += code_before + code + code_after;
tR += `# Results\n`;
tR += `Runtime:: ${get_regex(runtime_re, end_cleanup)}\n`;
tR += `Runtime Faster Than:: ${get_regex(faster_re, end_cleanup)}\n`;
tR += `Memory:: ${get_regex(memory_re, end_cleanup)}\n`;
tR += `Memory Less Than:: ${get_regex(less_re, end_cleanup)}\n`;
tR += total_time ? `Time:: ${total_time}\n` : '';
tR += `# Notes\n`;