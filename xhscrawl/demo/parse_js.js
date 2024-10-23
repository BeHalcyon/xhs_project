const fs = require('fs');
const babelParser = require('@babel/parser');

// 读取 JavaScript 文件
const code = fs.readFileSync('./xhs.js', 'utf8');

// 解析为 AST
const ast = babelParser.parse(code, {
    sourceType: 'module', // 如果使用 ES6 模块
    plugins: ['jsx', 'typescript'], // 根据需要添加插件
    strictMode: false // 关闭严格模式解析
});

// 将 AST 转换为 JSON 字符串
const astJson = JSON.stringify(ast, null, 2);

// 保存为本地文件
fs.writeFileSync('ast.json', astJson, 'utf8');

console.log('AST 已保存为 ast.json 文件');

const babelTraverse = require('@babel/traverse').default;

babelTraverse(ast, {
    enter(path) {
//        if (path.isVariableDeclaration()) {
//            console.log('Variable declaration found:', path.node);
//        }
        if (path.isFunctionDeclaration()) {
            console.log('Function declaration found:', path.node);
        }
    }
});