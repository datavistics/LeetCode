var original = await tp.system.clipboard();
let mdSplitIndex = original.indexOf('\n\n');
let end_split_index = original.indexOf('\n# Success:');

let md = original.slice(0,mdSplitIndex);
let code = original.slice(mdSplitIndex,end_split_index);
let end = original.slice(end_split_index,original.length);

const md_before = "# Problem\n"
let md_cleanup = md.replaceAll('# ', '');
const md_after = "\n# Code\n```py\n";
const code_after = "```\n";
let end_cleanup = end.replaceAll("# ", '');

function get_regex(regex, input_str) {
    input_match = [...input_str.matchAll(regex)];
    console.log(input_match)
    return input_match[0][1]; // The function returns the product of p1 and p2
}

const topics_re = /Related Topics (.*) */g;
const topics_matches = get_regex(topics_re, md).split(" ");

const runtime_re = /Runtime:(\d+ ms)/g
const faster_re = /faster than ([^ ]+)/g
const memory_re = /Memory Usage:(.+?),/g
const less_re = /less than ([^ ]+)/g

tR += `---\n`;
tR += `tags: ${topics_matches}\n`
tR += `fileType: LeetCode\n`;
tR += `creationDate: ${tp.date.now('YYYY-MM-DD')} \n`;
tR += `---\n`;
tR += md_before + md_cleanup + md_after + code + code_after;
tR += `# Results\n`;
tR += `Runtime:: ${get_regex(runtime_re, end_cleanup)}\n`;
tR += `Runtime Faster Than:: ${get_regex(faster_re, end_cleanup)}\n`;
tR += `Memory:: ${get_regex(memory_re, end_cleanup)}\n`;
tR += `Memory Less Than:: ${get_regex(less_re, end_cleanup)}\n`;
tR += `# Notes\n`;