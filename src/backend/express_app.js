const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('./database/mongodb.py');
const accountRoutes = require('./user/account.py');
const authRoutes = require('./user/authentication.py');
const subscriptionRoutes = require('./user/subscription.py');
const agentRoutes = require('./ai/agent.py');
const creationRoutes = require('./ai/creation.py');
const interactionRoutes = require('./ai/interaction.py');
const analysisRoutes = require('./ai/analysis.py');
const marketplaceRoutes = require('./marketplace/marketplace.py');
const transactionRoutes = require('./marketplace/transaction.py');
const brandRoutes = require('./brand/brand.py');
const licensingRoutes = require('./brand/licensing.py');
const apiRoutes = require('./integration/api.py');
const partnershipRoutes = require('./integration/partnership.py');

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/account', accountRoutes);
app.use('/auth', authRoutes);
app.use('/subscription', subscriptionRoutes);
app.use('/agent', agentRoutes);
app.use('/creation', creationRoutes);
app.use('/interaction', interactionRoutes);
app.use('/analysis', analysisRoutes);
app.use('/marketplace', marketplaceRoutes);
app.use('/transaction', transactionRoutes);
app.use('/brand', brandRoutes);
app.use('/licensing', licensingRoutes);
app.use('/api', apiRoutes);
app.use('/partnership', partnershipRoutes);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

module.exports = app;