var ghpages = require('gh-pages');

ghpages.publish(
    'public', // path to public directory
    {
        branch: 'gh-pages',
        repo: 'https://github.com/dchirst/pretcrawl.git', // Update to point to your repository  
        user: {
            name: 'Dan Hirst', // update to use your name
            email: 'dan.hirst@os.uk' // Update to use your email
        }
    },
    () => {
        console.log('Deploy Complete!')
    }
)