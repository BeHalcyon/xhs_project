const fs = require('fs');
const babelParser = require('@babel/parser');
const babelGenerator = require('@babel/generator').default;

// 读取 JavaScript 文件并解析成 AST
const code = fs.readFileSync('xhs.js', 'utf8');
const ast = babelParser.parse(code, {
    sourceType: 'module', // 如果使用 ES6 模块
    plugins: ['jsx', 'typescript'], // 根据需要添加插件
    strictMode: false // 关闭严格模式解析
});

// 使用 babel-generator 生成 JavaScript 代码
const output = babelGenerator(ast, {}, code);

// 输出重新生成的 JavaScript 代码
console.log(output.code);

// 保存为本地文件
fs.writeFileSync('xhs_decrypt.js', output.code, 'utf8');