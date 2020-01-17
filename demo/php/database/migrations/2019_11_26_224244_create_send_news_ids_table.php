<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateSendNewsIdsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('send_news_ids', function (Blueprint $table) {
            $table->increments('id');
            $table->string('cwxid',255)->nullable(false)->comment('登陆微信号');
            $table->integer('newsid')->default(0)->comment('最新的消息id');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('send_news_ids');
    }
}
